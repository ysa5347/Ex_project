from django.contrib import admin
from .models import Article, User, User_Article_match

admin.site.register(Article)
admin.site.register(User)
admin.site.register(User_Article_match)

# Register your models here.
