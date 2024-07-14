from datetime import datetime

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Artist, Album, Song


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


# serializer overview
class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()


class ArtistSerializer(serializers.ModelSerializer):
    """ Automatically sets a pk field (ex : id :1"""

    class Meta:
        model = Artist
        fields = "__all__"


# class ArtistHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
#     """ Sets a url field instead of a pk field(ex: url: 'http://api.example.com/user/1"""
#
#     class Meta:
#         model = Artist
#         fields = "__all__"


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"

## serializer overview
# class CommentSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     content = serializers.CharField(max_length=200)
#     created = serializers.DateTimeField()
#
#     def create(self, validated_data):
#         return Comment(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.email = validated_data.get('email', instance)
#         instance.email = validated_data.get('email', instance)
