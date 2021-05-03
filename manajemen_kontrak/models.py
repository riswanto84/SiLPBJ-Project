from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
import random
from django.utils.crypto import get_random_string


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
        ('hari', 'hari'),
        ('minggu', 'minggu'),
        ('bulan', 'bulan'),
        ('tahun', 'tahun'),
    )

    nama_barang = models.CharField(max_length=500)
    merk = models.CharField(max_length=200, blank=True, null=True)
    tipe = models.CharField(max_length=200, blank=True, null=True)
    satuan = models.CharField(max_length=100, choices=CATEGORY)
    spesifikasi_dan_gambar = models.TextField(blank=True, null=True)

    def __str__(self):
        return '%s, %s' % (self.merk, self.tipe)


class Penyedia(models.Model):
    nama_perusahaan = models.CharField(max_length=300)
    alamat_perusahaan = models.CharField(max_length=500)
    email = models.CharField(max_length=100, blank=True, null=True)
    npwp_perusahaan = models.CharField(max_length=15, null=True, blank=True)
    nomor_rekening = models.CharField(max_length=100, null=True, blank=True)
    bank = models.CharField(max_length=200, null=True, blank=True)
    direktur = models.CharField(max_length=300)
    no_telepon = models.CharField(max_length=50, blank=True, null=True)
    no_hp = models.CharField(max_length=50, blank=True, null=True)
    keterangan = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nama_perusahaan


class Kontrak(models.Model):
    JENIS_PEKERJAAN = (
        ('Pengadaan Barang', 'Pengadaan Barang'),
        ('Pekerjaan Konstruksi', 'Pekerjaan Konstruksi'),
        ('Jasa konsultan', 'Jasa konsultan'),
        ('Jasa lainnya', 'Jasa lainnya'),
    )

    BENTUK_KONTRAK = (
        ('Surat Perjanjian (kontrak)', 'Surat Perjanjian (kontrak)'),
        ('Surat Perintah Kerja', 'Surat Perintah Kerja'),
        ('Kuitansi', 'Kuitansi'),
        ('Surat Pesanan', 'Surat Pesanan'),
        ('Bukti Pembelian', 'Bukti Pembelian'),
    )

    CARA_PEMBAYARAN = (
        ('Bulanan', 'Bulanan'),
        ('Bertahap/Termin', 'Bertahap/Termin'),
        ('Sekaligus', 'Sekaligus'),
    )

    nomor_dipa = models.CharField(
        max_length=500, default='027.01.1.440140/2021')
    tanggal_dipa = models.DateField(default='2020-12-31')
    nomor_kontrak = models.CharField(max_length=200)
    judul_kontrak = models.CharField(max_length=500)
    tanggal_kontrak = models.DateField(default=datetime.now)
    tanggal_berakhir_kontrak = models.DateField(default=datetime.now)
    kode_kegiatan_output_akun = models.CharField(
        max_length=50, default='2228 / 995 / 532111')
    jenis_pekerjaan = models.CharField(
        max_length=100, choices=JENIS_PEKERJAAN, default='pengadaan barang')
    bentuk_kontrak = models.CharField(
        max_length=100, choices=BENTUK_KONTRAK, default='Surat Perintah Kerja')
    nilai_kontrak_terbilang = models.CharField(
        max_length=200, blank=True, null=True)
    cara_pembayaran = models.CharField(
        max_length=200, choices=CARA_PEMBAYARAN, default='Sekaligus')
    ketentuan_sanksi = models.CharField(max_length=500, blank=True, null=True,
                                        default='Denda 1 ‰ untuk setiap hari keterlambatan dari biaya / harga keseluruhan (sebelum PPn)')
    dibuat_oleh = models.ForeignKey(
        UserAdmin, on_delete=models.SET_NULL, null=True, blank=True)
    Penyedia = models.ForeignKey(Penyedia, on_delete=models.CASCADE)
    dokumen_pengadaan = models.FileField(
        max_length=255, upload_to='files/', blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)

    def __str__(self):
        return '%s, %s' % (self.nomor_kontrak, self.judul_kontrak)


class LampiranKontrak(models.Model):
    nomor_kontrak = models.ForeignKey(Kontrak, on_delete=models.CASCADE)
    barang = models.ForeignKey(Barang, on_delete=models.CASCADE)
    kuantitas = models.IntegerField()
    harga_satuan = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        unique_together = [['barang', ]]

    def __str__(self):
        return '%s %s, %s %s' % (self.barang.merk, self.barang.tipe,'Nomor Kontrak:', self.nomor_kontrak.nomor_kontrak)


class FotoItemPekerjaan(models.Model):
    item_pekerjaan = models.ForeignKey(
        LampiranKontrak, on_delete=models.CASCADE)
    file_foto = models.ImageField(default="profile.png", blank=True, null=True)

    def __str__(self):
        return '%s, %s' % (self.item_pekerjaan.nomor_kontrak, self.item_pekerjaan.barang.nama_barang)

class TandaTerimaDistribusi(models.Model):
    unique_id = get_random_string(length=8)
    nomor = str(random.randint(1000, 9999)) + "/" + str(unique_id)
   
    nomor_tanda_terima = models.CharField(max_length=100, default=nomor)
    tanggal_terima = models.DateField(default=datetime.now)
    peruntukan = models.CharField(max_length=250, null=True, blank=True)
    yang_menyerahkan = models.CharField(max_length=200, null=True, blank=True)
    yang_menerima = models.CharField(max_length=150, blank=True, null=True)
    kontrak = models.ForeignKey(Kontrak, on_delete=models.CASCADE)
    
    def __str__(self):
        return '%s %s %s, %s' % (self.nomor_tanda_terima, 'no. kontrak :', self.kontrak.nomor_kontrak, self.kontrak.judul_kontrak)

class LampiranTandaTerima(models.Model):
    nomor_tanda_terima = models.ForeignKey(TandaTerimaDistribusi, on_delete=models.CASCADE)
    barang = models.ForeignKey(Barang, on_delete=models.CASCADE)
    kuantitas = models.IntegerField()
    kondisi = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return '%s %s, %s %s, %s %s, %s %s %s' %  (self.barang.merk, self.barang.tipe, self.kuantitas, self.barang.satuan, "(No. Tanda Terima :", self.nomor_tanda_terima.nomor_tanda_terima, "No. Kontrak :", self.nomor_tanda_terima.kontrak.nomor_kontrak, ")")
