# Generated by Django 3.1.1 on 2021-05-04 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_kontrak', '0053_auto_20210504_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tandaterimadistribusi',
            name='nomor_tanda_terima',
            field=models.CharField(default='1524/RF3VXo2L', max_length=100),
        ),
    ]
