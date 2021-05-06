from django.shortcuts import render, HttpResponse, redirect, Http404

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *

from .forms import *
from django.forms import modelformset_factory, inlineformset_factory
from django.core.files.storage import FileSystemStorage
from crispy_forms.helper import FormHelper

# Create your views here.


def under_contructions(request):
    raise Http404('Under construction')


def master_template(request):
    return render(request, 'manajemen_kontrak/master_template.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home_dashboard')
        else:
            messages.info(request, 'Username atau Password tidak valid!')
    context = {}
    return render(request, 'manajemen_kontrak/login_page.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login_page')


@login_required(login_url='administrator')
def accountSettings(request):
    user = request.user.useradmin
    form = UserAdminForm(instance=user)
    # print(form)

    if request.method == 'POST':
        form = UserAdminForm(request.POST, request.FILES, instance=user)
        if form.is_valid:
            form.save()
            messages.info(request, 'Data berhasil diubah')

    context = {'form': form}
    return render(request, 'manajemen_kontrak/account_settings.html', context)


@login_required(login_url='administrator')
def home_dashboard(request):
    total_barang = Barang.objects.all().count()
    total_penyedia = Penyedia.objects.all().count()
    total_kontrak = Kontrak.objects.all().count()
    context = {
        'total_barang': total_barang,
        'total_penyedia': total_penyedia,
        'total_kontrak': total_kontrak,
    }
    return render(request, 'manajemen_kontrak/MenuDashboardMK.html', context)

# fitur barang


@login_required(login_url='administrator')
def EntryBarang(request):
    form = FormEntryBarang
    data_barang = Barang.objects.all().order_by('-id')

    if request.method == 'POST':
        form = FormEntryBarang(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Data berhasil disimpan')
            return redirect('EntryBarang')

    context = {
        'data_barang': data_barang,
        'form': form,
    }
    return render(request, 'manajemen_kontrak/FormEntryBarang.html', context)


@login_required(login_url='administrator')
def detail_barang(request, pk):
    detail_barang = Barang.objects.get(id=pk)
    context = {
        'detail_barang': detail_barang,
    }
    return render(request, 'manajemen_kontrak/detail_barang.html', context)


@login_required(login_url='administrator')
def ubah_barang(request, pk):
    barang = Barang.objects.get(id=pk)
    form = FormEntryBarang(instance=barang)

    if request.method == 'POST':
        form = FormEntryBarang(request.POST, instance=barang)
        form.save()
        messages.info(request, 'Data berhasil diubah')
        return redirect('EntryBarang')

    context = {
        'form': form,
    }
    return render(request, 'manajemen_kontrak/ubah_barang.html', context)


@login_required(login_url='administrator')
def hapus_barang(request, pk):
    barang = Barang.objects.get(id=pk)
    barang.delete()
    messages.info(request, 'Data berhasil dihapus')
    return redirect('EntryBarang')

# Fitur penyedia


def EntryPenyedia(request):
    form = FormEntryPenyedia
    data_penyedia = Penyedia.objects.all().order_by('-id')

    if request.method == 'POST':
        form = FormEntryPenyedia(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Data berhasil disimpan')
            return redirect('EntryPenyedia')

    context = {
        'data_penyedia': data_penyedia,
        'form': form,
    }
    return render(request, 'manajemen_kontrak/FormEntryPenyedia.html', context)


@login_required(login_url='administrator')
def detail_penyedia(request, pk):
    detail_penyedia = Penyedia.objects.get(id=pk)
    context = {
        'detail_penyedia': detail_penyedia,
    }
    return render(request, 'manajemen_kontrak/detail_penyedia.html', context)


@login_required(login_url='administrator')
def ubah_penyedia(request, pk):
    penyedia = Penyedia.objects.get(id=pk)
    form = FormEntryPenyedia(instance=penyedia)

    if request.method == 'POST':
        form = FormEntryPenyedia(request.POST, instance=penyedia)
        form.save()
        messages.info(request, 'Data berhasil diubah')
        return redirect('EntryPenyedia')

    context = {
        'form': form,
    }
    return render(request, 'manajemen_kontrak/ubah_penyedia.html', context)


@login_required(login_url='administrator')
def hapus_penyedia(request, pk):
    penyedia = Penyedia.objects.get(id=pk)
    penyedia.delete()
    messages.info(request, 'Data berhasil dihapus')
    return redirect('EntryPenyedia')

# Fitur penyedia


@login_required(login_url='administrator')
def EntryKontrak(request):
    if request.method == 'POST':
        tahun = request.POST.get('tahun_anggaran')
        kontrak = Kontrak.objects.filter(tahun_anggaran=tahun)
        messages.info(request, 'Menampilkan data kontrak tahun ' + tahun)
        context = {
            'kontrak': kontrak,
        }
        return render(request, 'manajemen_kontrak/FormEntryKontrak.html', context)

    tahun = datetime.now().year
    kontrak = Kontrak.objects.filter(tahun_anggaran=tahun).order_by('-id')
    context = {'kontrak': kontrak}
    return render(request, 'manajemen_kontrak/FormEntryKontrak.html', context)


@login_required(login_url='administrator')
def TambahKontrak(request):
    form = FormEntryKontrak
    if request.method == 'POST':
        form = FormEntryKontrak(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'Data kontrak berhasil disimpan')
            return redirect('EntryKontrak')

    context = {
        'form': form,
    }
    return render(request, 'manajemen_kontrak/FormTambahKontrak.html', context)


@login_required(login_url='administrator')
def DetailKontrak(request, pk):
    detail_kontrak = Kontrak.objects.get(id=pk)
    context = {
        'detail_kontrak': detail_kontrak,
    }
    return render(request, 'manajemen_kontrak/detail_kontrak.html', context)


@login_required(login_url='administrator')
def ubah_kontrak(request, pk):
    kontrak = Kontrak.objects.get(id=pk)
    form = FormEntryKontrak(instance=kontrak)

    if request.method == 'POST':
        form = FormEntryKontrak(request.POST, request.FILES, instance=kontrak)
        if form.is_valid:
            form.save()
            messages.info(request, 'Data berhasil diubah')
            return redirect('EntryKontrak')

    context = {'form': form}
    return render(request, 'manajemen_kontrak/FormTambahKontrak.html', context)


@login_required(login_url='administrator')
def hapus_kontrak(request, pk):
    kontrak = Kontrak.objects.get(id=pk)
    kontrak.delete()
    messages.info(request, 'Kontrak berhasil dihapus')
    return redirect('EntryKontrak')


@login_required(login_url='administrator')
def tambah_lampiran_kontrak(request, pk):
    kontrak = Kontrak.objects.get(id=pk)
    LampiranKontrakFormset = inlineformset_factory(
        Kontrak, LampiranKontrak, fields=('barang', 'kuantitas', 'harga_satuan'), can_delete=False)

    if request.method == 'POST':
        formset = LampiranKontrakFormset(
            request.POST, request.FILES, instance=kontrak)
        if formset.is_valid():
            formset.save()
            messages.info(request, 'Data berhasil disimpan')
            context = {
                'detail_kontrak': kontrak,
            }
            return render(request, 'manajemen_kontrak/detail_kontrak.html', context)
            # return HttpResponse('berhasil disimpan')

    formset = LampiranKontrakFormset(instance=kontrak)
    context = {
        'formset': formset,
        'id': pk,
        'kontrak': kontrak
    }
    return render(request, 'manajemen_kontrak/tambah_barang_kontrak.html', context)

    # return HttpResponse('tes')
