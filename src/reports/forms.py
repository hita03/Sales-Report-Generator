from django import forms
from django.db.models import fields
from .models import Report


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('name','remarks')
