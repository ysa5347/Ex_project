from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializer, PostListSerializer
from .models import Post, User, User_Post_match


@api_view(['GET'])
def helloAPI(request):
    return Response("hello world!")

@api_view(['GET'])
def PostList(request):
    posts = Post.objects.all()
    serializer = PostListSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def PostView(request, pk):
    posts = Post.objects.get(id=pk)
    serializer = PostSerializer(posts, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def PostCreate(request, pk):
    serializer = PostSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
        print('valid update')
    else:
        print('invalid update')
    return Response(serializer.data)

@api_view(['PUT'])
def PostUpdate(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(instance=post, data=request.data)

    if serializer.is_valid():
        serializer.save()
        print('valid update')
    else:
        print('invalid update')
    return Response(serializer.data)

@api_view(['DELETE'])
def PostDelete(request, pk):
    post = Post.objects.get(id=pk)

    if post:
        post.delete()
        return Response("Deleted...")
    else:
        return Response("There has something problem")

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    

# Create your views here.
