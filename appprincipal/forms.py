from projpad.models import *
from django import forms
from django.forms import ModelForm
from projpad.models import *


class HistForm(forms.ModelForm):
    class Meta:
        model = Hist_voo2015
        fields = ['sigla', 'numVoo', 'situacao', 'tipoLinha',  'origem', 'destino']

class HistForm2016(forms.ModelForm):
    class Meta:
        model = Hist_voo2016
        fields = ['sigla', 'numVoo', 'situacao', 'tipoLinha',  'origem', 'destino']

class HistForm2017(forms.ModelForm):
    class Meta:
        model = Hist_voo2017
        fields = ['sigla', 'numVoo', 'situacao', 'tipoLinha', 'origem', 'destino']

class HistForm2018(forms.ModelForm):
    class Meta:
        model = Hist_voo2018
        fields = ['sigla', 'numVoo', 'situacao', 'tipoLinha',  'origem', 'destino'] 