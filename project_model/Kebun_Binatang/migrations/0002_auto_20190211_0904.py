# Generated by Django 2.1.5 on 2019-02-11 09:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Kebun_Binatang', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penjaga',
            name='jadwal_jaga',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
