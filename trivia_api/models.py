from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=50)
    answer = models.CharField(max_length=25)
    category = models.CharField(max_length=25)