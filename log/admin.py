from django.contrib import admin
from .models import VerifyUser

@admin.register(VerifyUser)
class VerifyUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'balance', 'profile_picture', 'created']

