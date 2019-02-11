from django.contrib import admin
from .models import Direksi, Mentee, Mentor, Mata_pelajaran, Challenge, Live_code


# Register your models here.
my_mode = [Direksi, Mentee, Mentor, Mata_pelajaran, Challenge, Live_code]
admin.site.register(my_mode)
