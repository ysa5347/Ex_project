from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post, User, User_Post_match

class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    queryset = User.objects.all()
    queryset = User_Post_match.objects.all()

# Create your views here.
