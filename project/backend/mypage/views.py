from account.models import CustomUser
from django.http import HttpRequest
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getUser(request):
    pass

@api_view(['GET'])
def getUserArticle(request):
    pass

# Create your views here.
