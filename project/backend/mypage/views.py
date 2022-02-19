from django.http import HttpRequest
from django.shortcuts import redirect, render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import getUserSerializer
import time
from account.models import CustomUser

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
    pass

@api_view(['GET'])
def getUserPtcp(request):
    pass
