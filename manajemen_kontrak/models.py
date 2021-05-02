from datetime import datetime
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
        ('hari', 'hari'),
        ('minggu', 'minggu'),
        ('bulan', 'bulan'),
        ('tahun', 'tahun'),
    )

    nama_barang = models.CharField(max_length=500)
    merk = models.CharField(max_length=200, blank=True, null=True)
    tipe = models.CharField(max_length=200, blank=True, null=True)
    satuan = models.CharField(max_length=100, choices=CATEGORY)
    spesifikasi = models.TextField(blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nama_barang


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
        return '%s %s, %s' % ('Nomor Kontrak:', self.nomor_kontrak.nomor_kontrak, self.barang.nama_barang)
