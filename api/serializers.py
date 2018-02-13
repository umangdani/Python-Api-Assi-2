from rest_framework.response import Response
from rest_framework import serializers
from ApiApp.models import *
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate, login, logout
import datetime


class DiscussionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Discussion



class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		exclude = ('created_date', 'modified_date') 

 
 

