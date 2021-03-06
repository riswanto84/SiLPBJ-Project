# Generated by Django 3.1.1 on 2021-05-03 01:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_kontrak', '0037_fotoitempekerjaan'),
    ]

    operations = [
        migrations.CreateModel(
            name='TandaTerimaDistribusi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomor_tanda_terima', models.CharField(max_length=100)),
                ('tanggal_terima', models.DateField(default=datetime.datetime.now)),
                ('peruntukan', models.CharField(blank=True, max_length=250, null=True)),
                ('kondisi', models.CharField(blank=True, max_length=150, null=True)),
                ('yang_menyerahkan', models.CharField(blank=True, max_length=200, null=True)),
                ('yang_menerima', models.CharField(blank=True, max_length=150, null=True)),
                ('barang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manajemen_kontrak.barang')),
                ('kontrak', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manajemen_kontrak.kontrak')),
                ('kuantitas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manajemen_kontrak.lampirankontrak')),
            ],
        ),
    ]
