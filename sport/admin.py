from django.contrib import admin
from .models import Section, Game, Player, Team

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'team']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['id', 'section', 'team1', 'team2','win','draw','lose']
    