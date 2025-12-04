from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.TextField()
    answers = models.JSONField(default=list)
    correct_answer = models.CharField(max_length=32)
    category = models.CharField(max_length=32)
    difficulty = models.CharField(max_length=32)

class User(models.Model):
    user_name = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    points = models.IntegerField()
    difficulty = models.CharField(max_length=32)
    category = models.CharField(max_length=32)