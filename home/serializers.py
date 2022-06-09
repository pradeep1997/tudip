from rest_framework.authtoken.models import Token
from rest_framework import serializers
from django.template import loader
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status as status_code
from django.contrib.auth import authenticate
from django.contrib.auth.models import Permission, Group
from .models import *


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		exclude = ('user_permissions','groups','password','is_staff','is_superuser','date_joined')

class applicantSerializer(serializers.ModelSerializer):
	name = serializers.SerializerMethodField('get_name')
	class Meta:
		model = Applicant
		fields = ('name','mobile','email','address')

	def get_name(self, obj):
		if obj.fname and obj.lname:
			return str(obj.fname)+' '+str(obj.lname)
		return obj.fname