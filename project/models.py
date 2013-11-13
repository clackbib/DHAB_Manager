from django.db import models
from login.models import Profile



class Project(models.Model):
    creator = models.ForeignKey(Profile)
    name = models.CharField(max_length=30)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(null = True)
    end_date = models.DateField(null = True)
    project_mode =models.CharField(max_length=30, default="Organic")

    def __unicode__(self):
        return "Project {0} created by {1} on {2}.".format(self.name, self.creator, self.creation_date)

class MileStone(models.Model):
    name = models.CharField(max_length=30)
    project = models.ForeignKey(Project)
    description = models.TextField()
    start_date = models.DateField()
    creation_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField()

    def __unicode__(self):
        return self.name

class Requirements(models.Model):
    milestone = models.ForeignKey(MileStone, null=True, blank=True)
    project = models.ForeignKey(Project)
    creator = models.ForeignKey(Profile, related_name="requirement_creator")
    name = models.CharField(max_length=100)
    description  = models.TextField();
    technique = models.CharField(max_length=30)
    size_estimate = models.PositiveIntegerField()
    current_completion = models.PositiveIntegerField(default=0)
    requirement_type = models.CharField(max_length=30)
    creation_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()
    assignment = models.ManyToManyField(Profile, through= 'Assignment')

    def __unicode__(self):
        return "Requirement {0} from project : {1}".format(self.id, self.project.name)

class Assignment(models.Model):
    project = models.ForeignKey(Project, related_name="project_assign")
    requirement = models.ForeignKey(Requirements,related_name="req_assoc")
    profile = models.ForeignKey(Profile, related_name="assigned_user")
    role = models.CharField(max_length=30)
    productivity = models.PositiveIntegerField(default=0)
    task = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "Worker {0} on requirement {1}".format(self.profile.user.username, self.requirement.name)