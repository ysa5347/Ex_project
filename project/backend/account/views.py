from django.shortcuts import redirect, render
from rest_framework import status
from django.contrib.auth.hashers import check_password
from django.contrib import auth
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import time

from .serializers import UserCreateSerializer, UserLoginSerializer
from .models import CustomUser

@api_view(['GET'])
def IsIdValid(request):
    userID = request.GET['userID'] #?userID= form으로 쿼리스트링 받기
    try: #이미 존재하는 ID인 경우
        isEx = CustomUser.objects.get(userID=userID)
    except: #DB에 저장되어 있지 않은 새로운 ID인 경우
        isEx = None
    if isEx is None:
        overlap = True
    else:
        overlap = False
    context = {'IsIdValid': overlap}
    return Response(context)

@api_view(['POST'])
@permission_classes([AllowAny])
def createUser(request):
    if request.method == 'POST':
        serializer = UserCreateSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)

        if CustomUser.objects.filter(userID=serializer.validated_data['userID']).first() is None:
            serializer.save()
            return Response({"message": "ok"}, status=status.HTTP_201_CREATED)
        return Response({"message": "duplicate email"}, status=status.HTTP_409_CONFLICT)

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def loginUser(request):
    if request.method == 'GET':
        if request.session.session_key:
            Response({"message":"you're already loggined"}, status=status.HTTP_208_ALREADY_REPORTED)
            time.sleep(1.00)
            return redirect('/')
        else:
            return Response({"message":"go to login page."}) # 로그인 페이지 render
    elif request.method == 'POST':
        serializer = UserLoginSerializer(data=request.data)
        if request.session.session_key:
            Response({"message":"you're already loggined"}, status=status.HTTP_208_ALREADY_REPORTED)
            time.sleep(1.00)
            return redirect('/')
        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)

        if not serializer.validated_data['userID']:
            return Response({'message': 'put userID'}, status=status.HTTP_409_CONFLICT)
        
        userID = serializer.validated_data['userID']
        try:
            user = CustomUser.objects.get(userID = userID)
        except CustomUser.DoesNotExist:
            return Response({'message':'ID does not exist.'}, status=status.HTTP_403_FORBIDDEN)

        print(f'{user.password}, {serializer.validated_data["userID"]}')
        if not check_password(serializer.validated_data['password'], user.password):
            return Response({'message':'invalid password'}, status=status.HTTP_403_FORBIDDEN)
        else:
            auth.login(request, user)
            response = {
                'success': 'True',
                'userID' : f'{user.userID}'
            }
            return Response(response, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def viewsession(request):
    if request.session.session_key:
        response = {
                "userID":f"{request.user}",
                "sessionID":f"{request.session.session_key}",
                "context":"OK"
        }
        return Response(response, status=status.HTTP_200_OK)
    else:
        return Response({"context":"you've been logouted"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def logoutUser(request):
    u = request.user
    auth.logout(request)
    return Response({'message':f'successfully logoutted {u}'}, status=status.HTTP_202_ACCEPTED)
