from rest_framework import serializers
from article.models import Article

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
