from rest_framework import serializers
from .models import Article, TimeTable, UserTimeMatchTable

class UserTimeMatchTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTimeMatchTable
        fields = ['ptcpUser', 'Timetable']

class ArticleTimeTableSerializer(serializers.ModelSerializer):
    ptcpTable = UserTimeMatchTableSerializer(many=True, read_only=True)
    class Meta:
        model = TimeTable
        fields = '__all__'
        extra_fields = ['ptcpTable']

class ArticleSerializer(serializers.ModelSerializer):
    timeTable = ArticleTimeTableSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
        extra_fields = ['timeTable']

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['pk','title', 'startDay', 'endDay', 'lab', 'reward']