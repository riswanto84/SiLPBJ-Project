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

        widgets = {
            'modified_by': forms.HiddenInput(),
            'created_by': forms.HiddenInput(),
        }


class FormEntryPenyedia(ModelForm):
    class Meta:
        model = Penyedia
        fields = '__all__'

        labels = {
            'npwp_perusahaan': _('NPWP Perusahaan'),
        }

        widgets = {
            'modified_by': forms.HiddenInput(),
            'created_by': forms.HiddenInput(),
        }


class DateInput(forms.DateInput):
    input_type = 'date'


class FormEntryKontrak(ModelForm, forms.Form):
    class Meta:
        model = Kontrak
        fields = '__all__'

        widgets = {
            'modified_by': forms.HiddenInput(),
            'created_by': forms.HiddenInput(),
            'made_on': DateInput(),
        }
