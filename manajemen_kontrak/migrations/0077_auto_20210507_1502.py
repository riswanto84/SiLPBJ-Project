# Generated by Django 3.1.1 on 2021-05-07 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_kontrak', '0076_auto_20210507_1457'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FotoItemPekerjaan',
        ),
        migrations.AlterField(
            model_name='tandaterimadistribusi',
            name='nomor_tanda_terima',
            field=models.CharField(default='9541/iuaQiYCY', max_length=100),
        ),
    ]
