from django.contrib import admin
from django.contrib.sessions.models import Session
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
    
# session db admin
class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']
    
admin.site.register(Session, SessionAdmin)
# Register your models here.
