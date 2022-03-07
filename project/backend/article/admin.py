from django.contrib import admin
from .models import Article, TimeTable, UserTimeMatchTable, SubjectTag


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'postDate', 'writerID')
    readonly_fields = ('hits','postDate', 'modifiedDate')
    fieldsets = (
        (None, {
            'fields': ('writerID', 'lab', 'title', ('postDate', 'modifiedDate'), ('startDay', 'endDay'), ('startBirth', 'endBirth'))
        }),
        ('keywords', {
            'fields': ('gender', 'isOffline', 'reward', 'location', 'subject')
        }),
        ('etc', {
            'fields': ('content', 'articleFile', 'articleImg', 'hits')
        })
    )
admin.site.register(TimeTable)
admin.site.register(Article, ArticleAdmin)
admin.site.register(SubjectTag)
admin.site.register(UserTimeMatchTable)

# Register your models here.
