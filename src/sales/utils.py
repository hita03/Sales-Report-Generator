import customers
import uuid, base64
from customers.models import Customer
from profiles.models import Profile
from io import BytesIO
import matplotlib.pyplot as plt
import seaborn as sns


def generate_code():
    code = str(uuid.uuid4()).replace('-','').upper()[:12]
    return code

def get_salesman_from_id(val):
    salesman = Profile.objects.get(id=val)
    return salesman.user.username

def get_customer_from_id(val):
    customer = Customer.objects.get(id=val)
    return customer

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_key(res_by):
    if res_by == '#1':
        key = 'transaction_id'

    elif res_by == '#2':
        key = 'created' 

    return key    

def get_chart(chart_type, data, results_by,**kwargs):

    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10,4))
    key = get_key(results_by)
    d = data.groupby(key,as_index=False)['total_price'].agg('sum')
    if chart_type == '#1':
        print("\nBar\n")
        #plt.bar(d[key], d['total_price'])
        sns.barplot(x=key,y='total_price',data=d)
        #plt.bar(data['transaction_id'], data['price'])

    elif chart_type == '#2':
        print("\nPie\n")

        plt.pie(data=d, x='total_price',labels=d[key].values)
        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        fig = plt.gcf()
  
        # Adding Circle in Pie chart
        fig.gca().add_artist(centre_circle)

    elif chart_type == '#3':
        print("\nLine\n") 
        plt.plot(d[key], d['total_price'])       
    else:
        print("invalid chart choice")

    plt.tight_layout()    
    chart = get_graph()
    return chart