# Generated by Django 3.1.1 on 2021-05-04 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_kontrak', '0049_auto_20210504_0814'),
    ]

    operations = [
        migrations.AddField(
            model_name='barang',
            name='spesifikasi_dan_gambar',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tandaterimadistribusi',
            name='nomor_tanda_terima',
            field=models.CharField(default='7670/HoRJ4Ojo', max_length=100),
        ),
    ]
