from django.db import models
from ckeditor.fields import RichTextField
import datetime
from django.utils import timezone


class Historico(models.Model):

    sigla = models.CharField(max_length=4, blank=False)
    numVoo = models.PositiveIntegerField(null=True)

    choices = (
        ('Realizada', 'Viagem Realizada'),
        ('Cancelada', 'Viagem Cancelada'),
    )

    situacao = models.CharField(max_length=10, choices=choices, default='Sem conhecimento')
    tipoLinha = models.CharField(max_length=50, default="Sem Dados")
    data_real = models.DateTimeField(null=True)
    origem = models.CharField(max_length=100, null=False,blank=False)
    destino = models.CharField(max_length=100, null=False,blank=False)


    def __str__(self):
        return 'Sigla: {0} numVoo: {1}'.format(self.sigla, self.numVoo)

class Hist_voo2015(Historico):
    pass

class Hist_voo2015_2(Historico):
    pass

class Hist_voo2015_3(Historico):
    pass

class Hist_voo2015_4(Historico):
    pass

class Hist_voo2015_5(Historico):
    pass

class Hist_voo2015_6(Historico):
    pass

class Hist_voo2015_7(Historico):
    pass

class Hist_voo2015_8(Historico):
    pass

class Hist_voo2015_9(Historico):
    pass

class Hist_voo2015_10(Historico):
    pass

class Hist_voo2015_11(Historico):
    pass

class Hist_voo2015_12(Historico):
    pass

class Hist_voo2016(Historico):
    pass

class Hist_voo2016_2(Historico):
    pass

class Hist_voo2016_3(Historico):
    pass

class Hist_voo2017(Historico):
    pass

class Hist_voo2018(Historico):
    pass

class Hist_voo2019(Historico):
    pass

from django.db import models


class Order(models.Model):
    product_category = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=50)
    shipping_cost = models.CharField(max_length=50)
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)
