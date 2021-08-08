from django.contrib import admin
from .models import Position, Sale, CSV

# Register your models here.
admin.site.register(Sale)
admin.site.register(Position)
admin.site.register(CSV)