from django.db import models
from login.models import Profile
class Project(models.Model):
    creator = models.ForeignKey(Profile)
    name = models.CharField(max_length=30)
    description = models.TextField()
    #contributors
