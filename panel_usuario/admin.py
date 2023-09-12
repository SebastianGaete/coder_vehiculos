from django.contrib import admin
from .models import User
# Register your models here.

@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'codigo_funcionario', 'grado',  'is_superuser']