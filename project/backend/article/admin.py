from django.contrib import admin
from .models import Article, User_Article_match


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('postDate', 'writerID')
    readonly_fields = ('hits',)
    fieldsets = (
        (None, {
            'fields': ('writerID', 'lab', 'title', 'postDate', ('startDay', 'endDay'), ('startBirth', 'endBirth'))
        }),
        ('keywords', {
            'fields': ('gender', 'isOffline', 'reward', 'location', 'subject')
        }),
        ('etc', {
            'fields': ('content', 'articleFile', 'articleImg', 'hits')
        })
    )

admin.site.register(Article, ArticleAdmin)
admin.site.register(User_Article_match)

# Register your models here.
