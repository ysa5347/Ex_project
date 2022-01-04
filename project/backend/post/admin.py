from django.contrib import admin
from .models import Post, User, User_Post_match

admin.site.register(Post)
admin.site.register(User)
admin.site.register(User_Post_match)

# Register your models here.
