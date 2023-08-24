from django.db import models
from django.forms import ModelForm


class CalcModel(models.Model):
    first_number = models.FloatField(verbose_name='число №1')
    second_number = models.FloatField(verbose_name='число №2')


