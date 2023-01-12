from django.contrib import admin
from .models import Department, Personal, Personalite

# Register your models here.
admin.site.register(Department)
admin.site.register(Personal)
admin.site.register(Personalite)