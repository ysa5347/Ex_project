from django.http import HttpRequest
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ArticleSerializer, ArticleListSerializer
from .models import Article, User, User_Article_match


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
        articles = Article.objects.get(id=pk)
    except Article.DoesNotExist:
        return Response('error 404: 요청하신 페이지는 삭제되었거나 존재하지 않습니다.', status=404)
    serializer = ArticleSerializer(articles, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def IsIdValid(request):
    userID = request.GET['userID'] #?userID= form으로 쿼리스트링 받기
    try: #이미 존재하는 ID인 경우
        isEx = User.objects.get(userID=userID)
    except: #DB에 저장되어 있지 않은 새로운 ID인 경우
        isEx = None
    if isEx is None:
        overlap = True
    else:
        overlap = False
    context = {'IsIdValid': overlap}
    return Response(context)

@api_view(['POST'])
def ArticleCreate(request, pk):
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
