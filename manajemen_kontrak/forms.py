from django.forms import ModelForm
from manajemen_kontrak.models import *
from django import forms
from django.utils.translation import ugettext_lazy as _


class FormEntryBarang(ModelForm):
    class Meta:
        model = Barang
        fields = '__all__'

        labels = {
            'nama_barang': _('Nama Barang'),
        }