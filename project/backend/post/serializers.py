from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        
class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'exp_start', 'exp_end', 'lab_name', 'reward']