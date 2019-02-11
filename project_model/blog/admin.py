from django.contrib import admin
from .models import post, Mentee

# Register your models here.
my_mode = [post, Mentee]
admin.site.register(my_mode)