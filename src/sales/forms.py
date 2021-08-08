from django import forms
 
CHART_CHOICES = (
    ('#1','Bar Chart'),
    ('#2','Pie Chart'),
    ('#3','Line Chart'),
)
RESULT_CHOICES =(
    ('#1','transaction'),
    ('#2','sales date'),

)
class SalesSearchForm(forms.Form):
    date_from = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    date_to = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    chart_type = forms.ChoiceField(choices=CHART_CHOICES)
    results_by = forms.ChoiceField(choices=RESULT_CHOICES)
