from rest_framework.serializers import ModelSerializer
from .models import Post,Comment,Like
from rest_framework import serializers

class PostSerializer(ModelSerializer):
    likes = serializers.IntegerField(source='likes_on_post',read_only=True)
    comment = serializers.IntegerField(source='comment_on_post',read_only=True)
    username = serializers.CharField(source='user.username',read_only=True)
    image_url = serializers.CharField(source='get_image_url', read_only=True)

    
    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(ModelSerializer):
        
    class Meta:
        model = Comment
        fields = '__all__'

class LikeSerializer(ModelSerializer):
    
    class Meta:
        model = Like
        fields = '__all__'