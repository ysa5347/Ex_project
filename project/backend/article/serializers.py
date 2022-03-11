from rest_framework import serializers
from .models import Article, TimeTable, UserTimeMatchTable

# <-- Article View -->
class UserTimeMatchTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTimeMatchTable
        fields = ['ptcpUser', 'Timetable']

class ArticleTimeTableSerializer(serializers.ModelSerializer):
    ptcpTable = serializers.StringRelatedField(many=True)
    class Meta:
        model = TimeTable
        exclude = ['article']

class ArticleSerializer(serializers.ModelSerializer):
    timeTable = ArticleTimeTableSerializer(many=True, read_only=True)

    def validate_date(self, data):
        """Check that startDay place before of endDay."""
        if data['startDay'] > data['endDay']:
            raise serializers.ValidationError("실험 종료일은 시작일보다 앞설 수 없습니다.")
        return data

    class Meta:
        model = Article
        fields = '__all__'



# <-- Article List -->
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['pk','title', 'startDay', 'endDay', 'lab', 'reward']