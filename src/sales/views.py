from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.list import ListView
from .models import Sale
from .forms import SalesSearchForm
import pandas as pd
import matplotlib
import threading
import seaborn as sns
from reports.forms import ReportForm
from .utils import get_customer_from_id, get_salesman_from_id, get_chart
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home_view(request):
    sales_df =None
    merged_df =None
    positions_df = None
    df =None
    chart = None
    no_data = None
    search_form = SalesSearchForm(request.POST or None)
    report_form = ReportForm()
    if request.method =='POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        results_by = request.POST.get('results_by')

        
        sale_qs = Sale.objects.filter(created__date__lte=date_to, created__date__gte=date_from)
        if len(sale_qs) >0:
            sales_df = pd.DataFrame(sale_qs.values())
            sales_df['customer_id'] = sales_df['customer_id'].apply(get_customer_from_id)
            sales_df['salesman_id'] = sales_df['salesman_id'].apply(get_salesman_from_id)
            sales_df['created'] = sales_df['created'].apply(lambda x: x.strftime("%b %d %Y, %I:%M %p")) 
            sales_df['updated'] = sales_df['updated'].apply(lambda x: x.strftime("%b %d %Y, %I:%M %p"))            
            
            #sales_df['sales_id'] = sales_df['id']

            positions_data =[]
            for sale in sale_qs:
                for pos in sale.get_positions():
                    obj ={
                        'position_id': pos.id,
                        'product': pos.product.name,
                        'quantity': pos.quantity,
                        'price':pos.price,
                        'sales_id': pos.get_sales_id(),
                        'chart': chart,
                    }
                    positions_data.append(obj)
            #print(sales_df['Created'],sales_df['updated'])
            print(sales_df,type(sales_df))
            
            positions_df =pd.DataFrame((positions_data))  
            #merged_df = pd.merge(sales_df, positions_df,on='Sales ID' )    
            #df =merged_df.groupby('transaction_id',as_index=False)['price'].agg('sum')
            #= pd.DataFrame(qs.get_positions())


            chart = get_chart(chart_type, sales_df, results_by)#, labels=df['transaction_id'].values)
            #print("chart",chart)
            
            sales_df.rename({'customer_id':'Customer','transaction_id':'Transaction ID','salesman_id':'Salesman','id':'Sales ID', 'total_price':'Total Price','created':'Created','updated':'Updated'},axis =1, inplace =True)
            sales_df = sales_df.to_html(index=False, justify='center').replace('<table border="1" class="dataframe">','<table class="table" style="text-align:center;">')
            #sales_df = sales_df.to_html(index=False).replace('<tr style="text-align: right;">','<tr style="text-align: center;">')

            positions_df = positions_df.to_html()
            print(sales_df)
            #df = df.to_html()
            
            #print(sales_df)
            
            

        else:
            no_data = "No data available in this time frame."

    context={
        'search_form':search_form,
        'report_form':report_form,
        'sales_df': sales_df,
        'positions_df': positions_df,
        #'merged_df':merged_df,
        #'df':df,
        'chart':chart,
        'no_data': no_data,

    }
    return render(request, 'sales/home.html',context)

class SaleListView(LoginRequiredMixin,ListView):
    model = Sale
    template_name = 'sales/main.html' 
    
class SaleDetailView(LoginRequiredMixin,DetailView):
    model = Sale
    template_name = 'sales/detail.html' 

def sale_list_view(request):
    qs =Sale.objects.all()
    return render(request,'sales/main.html',{'object_list':qs})

def sale_detail_view(request, pk):
    obj =Sale.objects.get(pk=pk)
    return render(request, 'sales/detail.html',{'object':obj})

        
