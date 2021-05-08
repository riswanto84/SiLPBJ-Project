from django.forms import ModelForm
from manajemen_kontrak.models import *
from django import forms
from django.utils.translation import ugettext_lazy as _


class UserAdminForm(ModelForm):
    class Meta:
        model = UserAdmin
        fields = '__all__'
        exclude = ['user']

        labels = {
            'nama': _('Nama Lengkap'),
            'no_hp': _('Nomor HP'),
            'email': _('Alamat Email'),
            'profil_pic': _('Foto Profil'),
        }


class FormEntryBarang(ModelForm):
    class Meta:
        model = Barang
        fields = '__all__'

        labels = {
            'nama_barang': _('Nama Barang'),
            'spesifikasi_dan_gambar': _('Spesifikasi'),
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


class FormEntryKontrak(ModelForm, forms.Form):
    class Meta:
        model = Kontrak
        fields = '__all__'

        labels = {
            'nomor_dipa': _('Nomor DIPA'),
            'tanggal_dipa': _('Tanggal DIPA'),
            'nomor_kontrak': _('Nomor kontrak'),
            'kode_kegiatan_output_akun': _('Kode Kegiatan/Output/Akun'),
        }

        widgets = {
            'modified_by': forms.HiddenInput(),
            'created_by': forms.HiddenInput(),
        }


class FormLampiranKontrak(ModelForm):
    class Meta:
        model = LampiranKontrak
        fields = '__all__'

        widgets = {
            'modified_by': forms.HiddenInput(),
            'created_by': forms.HiddenInput(),
        }
