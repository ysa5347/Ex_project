
from account.models import CustomUser
from django.http import HttpRequest
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ArticleSerializer, ArticleListSerializer, ArticleTimeTableSerializer_read, ArticleTimeTableSerializer_write#, UserTimeMatchTableSerializer
from .models import Article, UserTimeMatchTable, TimeTable
from datetime import datetime, timedelta, timezone

KST = timezone(timedelta(hours=9))

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
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response('error 404: 요청하신 페이지는 삭제되었거나 존재하지 않습니다.', status=status.HTTP_404_NOT_FOUND)
    
    # <-- view 조회수 기능 -->
    article.hits += 1
    article.save()
    # <-- -->
    
    articleSerializer = ArticleSerializer(article, many=False)
    return Response(articleSerializer.data)

@api_view(['POST'])
def ArticleCreate(request):
    if request.method == 'POST':
        # 인증
        if not request.session.session_key:
            return Response('로그인이 필요한 요청입니다.', status=status.HTTP_403_FORBIDDEN)
        userID = request.user
        loginUser = CustomUser.objects.get(userID=userID)
        if not loginUser.isPermit:
            return Response('권한이 필요한 요청입니다.')
        
        # request data 변환
        data = request.data
        data['writerID'] = loginUser.pk
        # TTdata : list of timeTable.
        timeTableDatas = data.pop('timeTable')
        
        # Article 정보 저장
        articleSerializer = ArticleSerializer(data=data)
        if articleSerializer.is_valid() and articleSerializer.validate_date(data):
            articleSerializer.save()
        else:
            return Response(articleSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # timeTable 정보 저장
        articleID = Article.objects.latest('id').id
        for timeTableData in timeTableDatas:
            timeTableData['article'], timeTableData['numPtcp'] = articleID, 0
            timeTableSerializer = ArticleTimeTableSerializer_write(data=timeTableData)
            if timeTableSerializer.is_valid():
                timeTableSerializer.save()
            else:
                return Response(timeTableSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response('valid update', status=status.HTTP_200_OK)

@api_view(['POST', 'GET'])
def ArticlePtcp(request, pk):
    # 인증
    if not request.session.session_key:
        return Response('로그인이 필요한 요청입니다.', status=status.HTTP_403_FORBIDDEN)
    userID = request.user
    loginUser = CustomUser.objects.get(userID=userID)
    # 요청 실험 게시글
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response('error 404: 요청하신 페이지는 삭제되었거나 존재하지 않습니다.', status=status.HTTP_404_NOT_FOUND)

    # GET | 참여 가능한 timetable response
    if request.method == 'GET':
        timeTableDatas = TimeTable.objects.filter(article=article.pk)
        res = []
        for timeTableData in timeTableDatas:
            timeTableData = ArticleTimeTableSerializer_read(timeTableData).data
            del timeTableData['ptcpTable']
            timeTableData['start'] = timeTableData['start'][:-3] + timeTableData['start'][-2:]

            if datetime.strptime(timeTableData['start'], '%Y-%m-%dT%H:%M:%S%z') < datetime.now(KST):
                continue
            elif timeTableData['numMax'] <= timeTableData['numPtcp']:
                continue
            else:
                res.append(timeTableData)
        return Response(res)
            
    
    # POST | 참여 요망 timetable request
    elif request.method == 'POST':
        pass


    

@api_view(['PUT'])
def ArticleUpdate(request, pk):
    article = Article.objects.get(id=pk)
    serializer = ArticleSerializer(instance=article, data=request.data)

    if serializer.is_valid():
        serializer.save()
        print('valid update')
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        print('invalid update')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

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
