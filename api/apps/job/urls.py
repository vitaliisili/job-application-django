from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.job import views

app_name = 'job_application'

router = DefaultRouter()
router.register('jobs', views.JobApplicationViewSet, basename='jobs'),

urlpatterns = [
    path('', include(router.urls))
]