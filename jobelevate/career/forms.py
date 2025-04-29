from django import forms
from .models import CareerInterest

class CareerInterestForm(forms.Form):
    interest = forms.ModelChoiceField(
        queryset=CareerInterest.objects.all().order_by('name'),
        label="Select Career Interest",
        empty_label="Select an Interest"
    )