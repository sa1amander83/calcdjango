from django import forms
from django.forms import ModelForm

from calc.models import CalcModel


class CalcForm(ModelForm):
    class Meta:
        model=CalcModel

        fields=['first_number','second_number']
        # first_number = forms.FloatField(verbose_name='число №1')
        # second_number = forms.FloatField(verbose_name='число №2')

