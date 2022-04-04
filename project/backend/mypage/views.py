from django.http import HttpRequest
from django.shortcuts import redirect, render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import getUserSerializer, getUserArticleSerializer,getUserPtcpSerializer, getUserPtcpTimeSerializer
import time
from account.models import CustomUser
from article.models import Article, TimeTable, UserTimeMatchTable

@api_view(['GET'])
def getUser(request):
    try:
        User = CustomUser.objects.get(userID = request.user)    
    except:
        Response('please loggin!', status=status.HTTP_403_FORBIDDEN)
        time.sleep(1)
        return redirect('/account/login/')
    
    serializer = getUserSerializer(User, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getUserArticle(request):
    if not request.session.session_key:
        return Response('로그인이 필요한 요청입니다.', status=status.HTTP_403_FORBIDDEN)
    userID = request.user
    loginUser = CustomUser.objects.get(userID=userID)
    data = Article.objects.filter(writerID=loginUser.pk)
    serializer = getUserArticleSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUserPtcp(request):
    if not request.session.session_key:
        return Response('로그인이 필요한 요청입니다.', status=status.HTTP_403_FORBIDDEN)
    userID = request.user
    loginUser = CustomUser.objects.get(userID=userID)
    matchtableData = UserTimeMatchTable.objects.filter(userID=userID)
    # timetableData = TimeTable.objects.filter(ptcpUser=userID)
    serializer = getUserPtcpSerializer(matchtableData, many=True)
    return Response(serializer.data)
