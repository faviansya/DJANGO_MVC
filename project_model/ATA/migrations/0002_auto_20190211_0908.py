# Generated by Django 2.1.5 on 2019-02-11 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ATA', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direksi',
            name='nomor_telepon',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='mentee',
            name='nomor_telepon',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='nomor_telepon',
            field=models.CharField(max_length=255),
        ),
    ]
