# Generated by Django 3.1.1 on 2021-05-06 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_kontrak', '0069_auto_20210506_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tandaterimadistribusi',
            name='nomor_tanda_terima',
            field=models.CharField(default='4788/dBtylQHZ', max_length=100),
        ),
    ]
