# Generated by Django 3.1.1 on 2021-05-02 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_kontrak', '0006_auto_20210501_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kontrak',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomor_kontrak', models.CharField(max_length=200)),
                ('judul_kontrak', models.CharField(max_length=500)),
                ('kode_mak', models.CharField(max_length=50)),
                ('jenis_pekerjaan', models.CharField(choices=[('pengadaan barang', 'pengadaan barang'), ('pekerjaan konstruksi', 'pekerjaan konstruksi'), ('jasa konsultan', 'jasa konsultan'), ('jasa lainnya', 'jasa lainnya')], max_length=100)),
                ('bentuk_kontrak', models.CharField(choices=[('Surat Perjanjian', 'Surat Perjanjian'), ('Surat Perintah Kerja', 'Surat Perintah Kerja'), ('Kuitansi', 'Kuitansi'), ('Surat Pesanan', 'Surat Pesanan'), ('Bukti Pembelian', 'Bukti Pembelian')], max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='barang',
            name='satuan',
            field=models.CharField(choices=[('unit', 'unit'), ('buah', 'buah'), ('ls', 'ls')], max_length=100),
        ),
        migrations.DeleteModel(
            name='FotoBarang',
        ),
    ]
