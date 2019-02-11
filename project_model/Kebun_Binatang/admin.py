from django.contrib import admin
from .models import Hewan, Kandang, Penjaga, Pengunjung

# Register your models here.
my_mode = [Hewan, Kandang, Penjaga, Pengunjung]
admin.site.register(my_mode)