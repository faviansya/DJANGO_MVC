from django.db import models
from datetime import datetime
from datetime import date
from django.utils import timezone

# Create your models here.
class Dokter(models.Model):
    nama = models.CharField(max_length=255)
    nomor_telepon = models.CharField(max_length=255)
    bidang = models.CharField(max_length=255, default = '')
    jadwal_praktek = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nama

class Pasien(models.Model):
    nama = models.CharField(max_length=255)
    nomor_telepon = models.CharField(max_length=255)
    alamat = models.TextField(max_length=255)
    keluhan = models.CharField(max_length=255)

    def __str__(self):
        return self.nama


class Resep(models.Model):
    nama = models.CharField(max_length=255)
    total_harga = models.PositiveIntegerField()	
    kumpulan_obat = models.CharField(max_length=255)

    def __str__(self):
        return self.nama

class Obat(models.Model):
    nama = models.CharField(max_length=255)
    kandungan = models.TextField(max_length=255)
    khasiat = models.TextField(max_length=255)

    def __str__(self):
        return self.nama