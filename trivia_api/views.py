from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import QuestionSerializer
from .models import Question

class QuestionList(generics.ListCreateAPIView):
	queryset = Question.objects.all().order_by('id')
	serializer_class = QuestionSerializer

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Question.objects.all().order_by('id')
	serializer_class = QuestionSerializer