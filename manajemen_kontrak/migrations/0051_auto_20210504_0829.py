# Generated by Django 3.1.1 on 2021-05-04 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_kontrak', '0050_auto_20210504_0828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barang',
            name='merk',
        ),
        migrations.RemoveField(
            model_name='barang',
            name='nama_barang',
        ),
        migrations.RemoveField(
            model_name='barang',
            name='satuan',
        ),
        migrations.RemoveField(
            model_name='barang',
            name='spesifikasi_dan_gambar',
        ),
        migrations.RemoveField(
            model_name='barang',
            name='tipe',
        ),
        migrations.AlterField(
            model_name='tandaterimadistribusi',
            name='nomor_tanda_terima',
            field=models.CharField(default='1533/80XKX6uq', max_length=100),
        ),
    ]
