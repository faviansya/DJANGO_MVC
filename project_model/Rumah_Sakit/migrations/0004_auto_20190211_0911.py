# Generated by Django 2.1.5 on 2019-02-11 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rumah_Sakit', '0003_auto_20190211_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasien',
            name='nomor_telepon',
            field=models.CharField(max_length=255),
        ),
    ]
