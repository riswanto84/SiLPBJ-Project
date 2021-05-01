from django.db import models
from django.contrib.auth.models import User


class UserAdmin(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nama = models.CharField(max_length=200)
    no_hp = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    profil_pic = models.ImageField(
        default="profile.png", blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama


class Barang(models.Model):
    CATEGORY = (
        ('unit', 'unit'),
        ('buah', 'buah'),
        ('ls', 'ls'),
    )

    nama_barang = models.CharField(max_length=500)
    merk = models.CharField(max_length=200, blank=True, null=True)
    tipe = models.CharField(max_length=200, blank=True, null=True)
    satuan = models.CharField(max_length=100, choices=CATEGORY)
    spesifikasi = models.TextField(blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nama_barang


class FotoBarang(models.Model):
    deskripsi = models.CharField(max_length=200, blank=True, null=True)
    nama_barang = models.ForeignKey(Barang, on_delete=models.CASCADE)
    foto = models.ImageField(default="no-image.png", blank=True, null=True)

    def __str__(self):
        return self.deskripsi


class Penyedia(models.Model):
    nama_perusahaan = models.CharField(max_length=300)
    alamat_perusahaan = models.TextField()
    email = models.CharField(max_length=100, blank=True, null=True)
    npwp_perusahaan = models.CharField(max_length=15)
    direktur_utama = models.CharField(max_length=300)
    no_telepon = models.CharField(max_length=50, blank=True, null=True)
    no_hp = models.CharField(max_length=50, blank=True, null=True)
    keterangan = models.TextField()

    def __str__(self):
        return self.nama_perusahaan
