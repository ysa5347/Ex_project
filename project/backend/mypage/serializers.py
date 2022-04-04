from rest_framework import serializers
from article.models import Article, TimeTable

class getUserSerializer(serializers.Serializer):
    userID = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    phone = serializers.CharField(required=False)
    penalty = serializers.IntegerField(required=True)
    birth = serializers.IntegerField(required=True)
    name = serializers.CharField(required=True)
    dateJoined = serializers.DateTimeField(required=True)
    isPermit = serializers.BooleanField(required=True)
    if isPermit == 1:
        lab = serializers.CharField(required=True)

class getUserArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['pk','title', 'startDay', 'endDay', 'lab', 'reward']

# <-- 작업 영역 --> 
"""
특정 Article을 참조하는 모든 TimeTable과 UserMatchTable을 역참조해야했던 ArticleView와는 반대로,
특정 UserMatchTable이 참조하는 하나의 TimeTable, Article을 순차적으로 참조해야하기 때문에 
ArticleView와는 반대로 접근해야한다.

그런데 하나의 UserMatchTable에 대해서는 Serializer로 제공이 가능한데, view.py에서 filter로 복수로 받아들이면 어떻게 Serializer로 제공해야할지 모르겠다.
"""
class getUserPtcpTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeTable
        fields = '__all__'

class getUserPtcpSerializer(serializers.ModelSerializer):
    """
    출력해야 하는 것 : 내가 어떤 실험을, 언제, 어디에서, 몇시 사이에 참여했는지
    --> 어떤 Article의 어떤 TimeTable에 참가했는지 탐색
    """
    timetable = getUserPtcpTimeSerializer(many=True)
    class Meta:
        model = Article
        fields = ['pk','title', 'startDay', 'endDay', 'lab', 'reward']
# <-- -->