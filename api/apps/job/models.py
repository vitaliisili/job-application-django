from django.db import models
from django.contrib.auth import get_user_model
from apps.core.models import BaseModel

class JobApplication(BaseModel):
    user = models.ForeignKey(get_user_model(), related_name='jobs', on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=250)
    link = models.URLField()
    description = models.TextField(null=True)
    application_date = models.DateField(auto_now_add=True, editable=True)
