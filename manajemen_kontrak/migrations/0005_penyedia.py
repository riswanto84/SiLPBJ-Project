# Generated by Django 3.1.1 on 2021-04-30 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_kontrak', '0004_barang_keterangan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Penyedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_perusahaan', models.CharField(max_length=300)),
                ('alamat_perusahaan', models.TextField()),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('npwp_perusahaan', models.CharField(max_length=15)),
                ('direktur_utama', models.CharField(max_length=300)),
                ('no_telepon', models.CharField(blank=True, max_length=50, null=True)),
                ('no_hp', models.CharField(blank=True, max_length=50, null=True)),
                ('keterangan', models.TextField()),
            ],
        ),
    ]