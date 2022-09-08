from dataclasses import fields
from rest_framework import serializers
from .models import Article, TimeTable, UserTimeMatchTable

# <-- Article View -->
class UserTimeMatchTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTimeMatchTable
        fields = ['ptcpUser', 'Timetable']

class ArticleTimeTableSerializer_read(serializers.ModelSerializer):
    ptcpTable = serializers.StringRelatedField(many=True)
    class Meta:
        model = TimeTable
        exclude = ['article']

class ArticleTimeTableSerializer_write(serializers.ModelSerializer):
    class Meta:
        model = TimeTable
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    timeTable = ArticleTimeTableSerializer_read(many=True, read_only=True)

    def validate_date(self, data):
        """Check that startDay place before of endDay."""
        if data['startDay'] > data['endDay']:
            raise serializers.ValidationError("실험 종료일은 시작일보다 앞설 수 없습니다.")
        if data['startBirth'] and data['endBirth']:
            # print("pass")
            if data['startBirth'] > data['endBirth']:
                raise serializers.ValidationError("endBirth는 startBirth보다 앞설 수 없습니다.")
        elif data['startBirth'] or data['endBirth']: # startBirth, 혹은 endBirth 둘 중 하나만 입력된 경우엔 경고를 출력 할 것인가?
            raise serializers.ValidationError("startBirth, endBirth중 하나가 입력되지 않았습니다.")
        else:
            print("zero")
        return data

    class Meta:
        model = Article
        fields = '__all__'



# <-- Article List -->
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['pk','title', 'startDay', 'endDay', 'lab', 'reward']