from django.db import models
import datetime
from django.utils import timezone

class Project_Done(models.Model):
    Work = models.CharField(max_length=200, default='None')
    WorkText = models.CharField(max_length=200, default='None')
    Date_Create = models.DateTimeField('date created')

    def __str__(self):
        return self.Work

class Skill(models.Model):
    Skill = models.CharField(max_length=200, default='None')
    Skill_Text = models.CharField(max_length=200, default='None')
    Image = models.ImageField(upload_to="default/upload_image/", blank=True, null=True)
    Date_Create = models.DateTimeField('date created')

    def __str__(self):
        return self.About

class Visitor_Email(models.Model):
    Visitor_Email = models.CharField(max_length=200, default='None')
    Date_Create = models.DateTimeField('date created')

    def __str__(self):
        return self.Visitor_Email
    