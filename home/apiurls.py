from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as token_view
from . import api

router = DefaultRouter()
router.register('users', api.UsersViewSet)
router.register('Applicants', api.ApplicantViewSet, basename='applicants')


urlpatterns = [
]