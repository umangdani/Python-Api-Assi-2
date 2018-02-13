
from rest_framework import serializers
from ApiApp.models import *

class DiscussionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discussion

class SearchDiscssionsSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
