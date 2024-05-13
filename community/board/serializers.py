from rest_framework import serializers
from .models import Community
from .models import Comment
from django.utils import timezone
class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ['id',  'title', 'body']
    
class CommunitySerializer2(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ['id', 'title', 'body','created_at']

class CommentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment']

class CommentResponseSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = '__all__'

    def get_created_at(self, obj):
        time = timezone.localtime(obj.created_at)
        return time.strftime('%Y-%m-%d')

class CommunityDetailSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    comments = CommentResponseSerializer(many=True, read_only=True)
    class Meta:
        model = Community
        fields = ['id', 'title', 'body','created_at','comments']

    def get_created_at(self, obj):
        time = timezone.localtime(obj.created_at)
        return time.strftime('%Y-%m-%d') 
