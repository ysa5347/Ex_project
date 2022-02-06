from django.contrib import admin
from . import models

@admin.register(models.CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'userID',
        'email',
        'date_joined',
    )
    list_display_links = (
        'userID',
        'email',
    )
# Register your models here.
