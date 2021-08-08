#import django
#django.setup()
#from django.db.models import sales
#from sales import signals
from django.apps import AppConfig
#from sales import signals


class SalesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sales'

    def ready(self):
       import sales.signals
       #return 