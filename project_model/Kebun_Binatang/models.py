from django.db import models
from datetime import datetime
from datetime import date
from django.utils import timezone

# Create your models here.
class Hewan(models.Model):
    nama = models.CharField(max_length=255)
    spesies = models.CharField(max_length=255)
    berat = models.CharField(max_length=255, default = '')
    umur = models.PositiveIntegerField()

    def __str__(self):
        return self.nama

class Kandang(models.Model):
    nama = models.CharField(max_length=255)
    isi_kandang = models.PositiveIntegerField()
    luas_kandang = models.PositiveIntegerField()

    def __str__(self):
        return self.nama


class Penjaga(models.Model):
    nama = models.CharField(max_length=255)
    nomor_telepon = models.CharField(max_length=255)
    jadwal_jaga = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nama

class Pengunjung(models.Model):
    nama = models.CharField(max_length=255)
    nomor_telepon = models.CharField(max_length=255)
    hari_berkunjung = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nama