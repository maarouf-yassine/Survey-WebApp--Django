from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    icon = models.CharField(max_length=100, null=True)
    users = models.CharField(max_length=500, default="")

    def __str__(self):
        return str(self.category_name)

class Survey(models.Model):
    title_name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subtitle = models.CharField(max_length=100, null=True)
    people = models.IntegerField(default=0)
    question = models.CharField(max_length=200, default="")
    agree = models.IntegerField(default=0)
    stronglyagree = models.IntegerField(default=0)
    neutral = models.IntegerField(default=0)
    disagree = models.IntegerField(default=0)
    stronglydisagree = models.IntegerField(default=0)

    def __str__(self):
        return str(self.title_name) + " | " + str(self.category)


class User(AbstractUser):
    points = models.IntegerField(default=0)

class SubmittedSurveys(models.Model):
    user = models.CharField(max_length=50)
    survey = models.CharField(max_length=100)
    question = models.CharField(max_length=200, default=".")
    answer = models.CharField(max_length=200, default=".")

    def __str__(self):
        return self.survey
