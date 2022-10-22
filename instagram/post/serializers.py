from rest_framework import serializers
from account.models import User
from . import models


class FeedAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'profile_photo'
        )


class CommentSerializer(serializers.ModelSerializer):
    author = FeedAuthorSerializer()

    class Meta:
        model = models.Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    comment_post = CommentSerializer(many=True, read_only=True)
    author = FeedAuthorSerializer()

    class Meta:
        model = models.Post
        fields = (
            'id',
            'image',
            'caption',
            'comment_post',
            'author'
        )