from reports.forms import ReportForm
from django.shortcuts import render, get_object_or_404
from profiles.models import Profile
from django.http import JsonResponse
from .utils import get_report_image
from .models import Report
from django.views.generic import ListView, DetailView, TemplateView
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from sales.models import Sale, Position, CSV
from products.models import Product
from customers.models import Customer
import csv
from django.utils.dateparse import parse_date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
class UploadTemplateView(LoginRequiredMixin,TemplateView):
    template_name='reports/from_file.html'


class ReportListView(LoginRequiredMixin,ListView):
    model = Report
    template_name ='reports/main.html'

class ReportDetailView(LoginRequiredMixin,DetailView):
    model = Report
    template_name = 'reports/detail.html'

@login_required
def create_report(request):
    form = ReportForm(request.POST or None)
    if request.is_ajax():
        #name = request.POST.get('name')
        #remarks = request.POST.get('remarks')
        image = request.POST.get('image')
        #name = request.POST.get('name')


        img = get_report_image(image)
        author =Profile.objects.get(user =request.user)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.image=img
            instance.author = author
            instance.save()
        #Report.objects.create(name=name, remarks=remarks,image=img,author=author)
        return  JsonResponse({'msg': 'send'})
    return JsonResponse({})    


@login_required
def csv_upload_view(request):
    print("\n-------i have entered upload view-----")
    if request.method == 'POST':
        csv_file_name = request.FILES.get('file').name
        csv_file = request.FILES.get('file')
        obj, created = CSV.objects.get_or_create(file_name = csv_file_name)
        if created:
            obj.csv_file = csv_file
            obj.save()
            print("hello")
            with open(obj.csv_file.path,'r') as f:
                reader = csv.reader(f)
                reader.__next__() #this way we will skip the 1st heading rows
                for row in reader:
                    #print(row, type(row))
                    data= "".join(row)
                    #print("\n\n",data)
                    #row.pop()
                    print(row[5],type(row[5]),"\n")
                    
                    transaction_id = row[1]
                    product = row[2]
                    quantity = int(row[3])
                    customer =row[4]
                    date = parse_date(row[5])
                    print(date,"!!!!!!!!11")

                    try:
                        product_obj =  Product.objects.get(name__iexact=product)
                    except Product.DoesNotExist:
                        product_obj = None

                    #print(product_obj)        
                    if product_obj is not None:
                        c_obj, _ = Customer.objects.get_or_create(name=customer) #this will be true for creating or false if it's getting it(already created)
                        p_obj = Position.objects.create(product=product_obj, quantity=quantity,created = date)
                        s_obj = Profile.objects.get(user=request.user)

                        sale_object, _ = Sale.objects.get_or_create(transaction_id= transaction_id, customer=c_obj,salesman=s_obj,created=date)
                        sale_object.positions.add(p_obj)
                return JsonResponse({'ex':False})
        else:
            return JsonResponse({'ex':True})              

    return HttpResponse()

@login_required
def render_pdf_view(request, pk):
    template_path = 'reports/pdf.html'
    obj = get_object_or_404(Report,pk=pk)
    #obj = Report.objects.get(pk=pk)
    context = {'obj': obj}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #if dl
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    #if display
    #response['Content-Disposition'] = 'filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response