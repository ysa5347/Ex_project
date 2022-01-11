from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializer
from .models import Post, User, User_Post_match


@api_view(['GET'])
def helloAPI(request):
    return Response("hello world!")

@api_view(['GET'])
def post_page(request, post_id):
    totalPost = Post.objects.all()
    return Response(totalPost())

class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    

# Create your views here.
