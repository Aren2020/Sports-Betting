from django.contrib import admin
from .models import Bets

@admin.register(Bets)
class BetsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'game',
                  'amount', 'user_choice', 'win_choice','created']
