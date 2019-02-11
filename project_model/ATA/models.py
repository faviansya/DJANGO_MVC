from django.db import models
from datetime import datetime
from datetime import date
from django.utils import timezone

# Create your models here.
class Direksi(models.Model):
    nama_lengkap = models.CharField(max_length=255)
    nomor_telepon = models.CharField(max_length=255)
    jabatan = models.CharField(max_length=255)

    def __str__(self):
        return self.nama_lengkap

class Mentee(models.Model):
    nama_lengkap = models.CharField(max_length=255)
    nomor_telepon = models.CharField(max_length=255)
    nomor_absen = models.PositiveIntegerField()
    nilai_ratarata = models.PositiveIntegerField()

    def __str__(self):
        return self.nama_lengkap

class Mata_pelajaran(models.Model):
    nama_pelajaran = models.CharField(max_length=255)
    jadwal_dimulai = models.DateTimeField(default=timezone.now)
    jadwal_berakhir = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nama_pelajaran

class Mentor(models.Model):
    nama_lengkap = models.CharField(max_length=255)
    nomor_telepon = models.CharField(max_length=255)
    mata_pelajaran = models.ForeignKey(Mata_pelajaran, on_delete = models.CASCADE, default='')

    def __str__(self):
        return self.nama_lengkap

class Challenge(models.Model):
    nama_challenge = models.CharField(max_length=255)
    banyak_soal = models.PositiveIntegerField()
    bobot_nilai = models.PositiveIntegerField()
    mata_pelajaran = models.ForeignKey(Mata_pelajaran, on_delete = models.CASCADE, default='')

    def __str__(self):
        return self.nama_challenge

class Live_code(models.Model):
    nama_live_code = models.CharField(max_length=255)
    banyak_soal = models.CharField(max_length=255)
    bobot_nilai = models.PositiveIntegerField()
    tanggal_pelaksanaan = models.DateField(default=date.today)
    mata_pelajaran = models.ForeignKey(Mata_pelajaran, on_delete = models.CASCADE, default='')

    def __str__(self):
        return self.nama_live_code

