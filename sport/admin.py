from django.contrib import admin
from .models import SportSection

@admin.register(SportSection)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'image']
    prepopulated_fields = {'slug': ('name',)}