from django.contrib import admin
from .models import ReportBolsa

# Register your models here.

@admin.register(ReportBolsa)
class ReportBolsa(admin.ModelAdmin):
    list_display = ('autor', 'titulo', 'texto', 'data_criacao', 'data_publicacao')