from django.http import HttpRequest
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ArticleSerializer, ArticleListSerializer
from .models import Article, UserTimeMatchTable, TimeTable


@api_view(['GET'])
def helloAPI(request):
    return Response("hello world!")

@api_view(['GET'])
def ArticleList(request):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def ArticleView(request, pk):
    try:
        articles = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response('error 404: 요청하신 페이지는 삭제되었거나 존재하지 않습니다.', status=status.HTTP_404_NOT_FOUND)
    
    # <-- view 조회수 기능 -->
    articles.hits += 1
    articles.save()
    # <-- -->
    serializer = ArticleSerializer(articles, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def ArticleCreate(request):
    serializer = ArticleSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
        print('valid update')
    else:
        print('invalid update')
    return Response(serializer.data)

@api_view(['PUT'])
def ArticleUpdate(request, pk):
    article = Article.objects.get(id=pk)
    serializer = ArticleSerializer(instance=article, data=request.data)

    if serializer.is_valid():
        serializer.save()
        print('valid update')
    else:
        print('invalid update')
    return Response(serializer.data)

@api_view(['DELETE'])
def ArticleDelete(request, pk):
    try:
        article = Article.objects.get(id=pk)
    except:
        return Response("There has something problem")

    article.delete()
    return Response("Deleted...")
    

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    

# Create your views here.
