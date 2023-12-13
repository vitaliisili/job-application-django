from rest_framework import viewsets
from apps.job.models import JobApplication
from apps.job.serializers import JobApplicationSerializer
from apps.job.permissions import JobApplicationPermissions


class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    permission_classes = (JobApplicationPermissions,)
    search_fields = ['$company_name', '$position']
    ordering_fields = ['application_date']
    ordering = ['-application_date']
