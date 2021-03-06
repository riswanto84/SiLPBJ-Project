# Generated by Django 3.1.1 on 2021-05-04 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manajemen_kontrak', '0051_auto_20210504_0829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fotoitempekerjaan',
            name='item_pekerjaan',
        ),
        migrations.RemoveField(
            model_name='kontrak',
            name='Penyedia',
        ),
        migrations.RemoveField(
            model_name='kontrak',
            name='dibuat_oleh',
        ),
        migrations.AlterUniqueTogether(
            name='lampirankontrak',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='lampirankontrak',
            name='barang',
        ),
        migrations.RemoveField(
            model_name='lampirankontrak',
            name='nomor_kontrak',
        ),
        migrations.RemoveField(
            model_name='lampirantandaterima',
            name='barang',
        ),
        migrations.RemoveField(
            model_name='lampirantandaterima',
            name='nomor_tanda_terima',
        ),
        migrations.RemoveField(
            model_name='tandaterimadistribusi',
            name='kontrak',
        ),
        migrations.RemoveField(
            model_name='useradmin',
            name='user',
        ),
        migrations.DeleteModel(
            name='Barang',
        ),
        migrations.DeleteModel(
            name='FotoItemPekerjaan',
        ),
        migrations.DeleteModel(
            name='Kontrak',
        ),
        migrations.DeleteModel(
            name='LampiranKontrak',
        ),
        migrations.DeleteModel(
            name='LampiranTandaTerima',
        ),
        migrations.DeleteModel(
            name='Penyedia',
        ),
        migrations.DeleteModel(
            name='TandaTerimaDistribusi',
        ),
        migrations.DeleteModel(
            name='UserAdmin',
        ),
    ]
