from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User

class Person(User):
	rg = models.CharField(max_length=20)

# Create your models here.
class Relatorio(models.Model):
    data_criacao = models.DateTimeField(default=timezone.now, blank=True)
    num_chamado = models.CharField(max_length=255, blank=True)
    sessp = models.CharField(max_length=255, blank=True)
    usuario = models.CharField(max_length=255, blank=True)
    coordenadoria = models.CharField(max_length=255, blank=True)
    setor = models.CharField(max_length=255, blank=True)
    predio = models.CharField(max_length=255, blank=True)
    sala = models.CharField(max_length=255, blank=True)
    ramal = models.CharField(max_length=255, blank=True)
    modelo = models.CharField(max_length=255, blank=True)
    cpu = models.CharField(max_length=255, blank=True)
    ram = models.CharField(max_length=255, blank=True)
    hd = models.CharField(max_length=255, blank=True)
    tecinic = models.CharField(max_length=255, blank=True)
    tecfim = models.CharField(max_length=255, blank=True)
    patrimonio = models.CharField(max_length=255, blank=True)
    serie = models.CharField(max_length=255, blank=True)
    obs = models.TextField()

    check1 = models.BooleanField(default=False)
    check2 = models.BooleanField(default=False)
    check3 = models.BooleanField(default=False)
    check4 = models.BooleanField(default=False)
    check5 = models.BooleanField(default=False)
    check6 = models.BooleanField(default=False)
    check7 = models.BooleanField(default=False)
    check8 = models.BooleanField(default=False)
    check9 = models.BooleanField(default=False)
    check10 = models.BooleanField(default=False)
    check11 = models.BooleanField(default=False)
    check12 = models.BooleanField(default=False)
    check13 = models.BooleanField(default=False)
    check14 = models.BooleanField(default=False)
    check15 = models.BooleanField(default=False)
    check16 = models.BooleanField(default=False)

class FormRelatorio(forms.ModelForm):
    class Meta:
        model = Relatorio
        fields = '__all__'