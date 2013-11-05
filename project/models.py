from django.db import models
from login.models import Profile


class Project(models.Model):
    creator = models.ForeignKey(Profile)
    name = models.CharField(max_length=30)
    description = models.TextField()

class Requirements(models.Model):
    project = models.ForeignKey(Project)
    creator = models.ForeignKey(Profile)
    name = models.CharField(max_length=100)
    description  = models.TextField();
    technique = models.CharField(max_length=30)
    size_estimate = models.PositiveIntegerField()
    effort_estimate = models.PositiveIntegerField()
    requirement_type = models.CharField(max_length=30)