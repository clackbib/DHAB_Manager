from django.db import models
from login.models import Profile


class Project(models.Model):
    creator = models.ForeignKey(Profile)
    name = models.CharField(max_length=30)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(null = True)
    end_date = models.DateField(null = True)


class Requirements(models.Model):
    project = models.ForeignKey(Project)
    creator = models.ForeignKey(Profile)
    name = models.CharField(max_length=100)
    description  = models.TextField();
    technique = models.CharField(max_length=30)
    size_estimate = models.PositiveIntegerField()
    current_completion = models.PositiveIntegerField(default=0)
    effort_estimate = models.PositiveIntegerField()
    requirement_type = models.CharField(max_length=30)
    creation_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField()

    def __unicode__(self):
        "Requirement {0} from project : {1}".format(self.id, self.project.name)