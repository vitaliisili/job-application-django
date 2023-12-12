from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.user import views

app_name = 'user_profile'

router = DefaultRouter()
router.register('users', views.UserViewSet, basename='users'),

urlpatterns = [
    path('', include(router.urls))
]
