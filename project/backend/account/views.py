from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from .serializers import UserCreateSerializer
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