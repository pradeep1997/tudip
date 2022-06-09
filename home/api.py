from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters import rest_framework as filters
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status as rest_status, generics, serializers, viewsets, mixins

from .serializers import *
from .models import *

class UsersViewSet(viewsets.ModelViewSet):
	queryset = User.objects.filter(is_active=True).all()
	serializer_class = UserSerializer
	filter_fields = ['email','mobile','phone','gender','dob',]
	http_method_names = ['get', 'post','put','patch']


class ApplicantViewSet(viewsets.ModelViewSet):
	permission_classes = ((AllowAny,))
	queryset = Applicant.objects.filter(status='Active').all()
	serializer_class = applicantSerializer
	filter_backends = [filters.SearchFilter, filters.OrderingFilter]
	search_fields = ['fname','mobile','email','designation',]
	ordering_fields = ['mobile', 'email', 'id']
	http_method_names = ['get', 'post','put','patch']