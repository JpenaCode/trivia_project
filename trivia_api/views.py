from django.shortcuts import render
from rest_framework import generics
from .models import Question, User
from .serializers import QuestionSerializer, UserSerializer

# Question views
class QuestionList(generics.ListCreateAPIView):
    serializer_class = QuestionSerializer
    
    def get_queryset(self):
        queryset = Question.objects.all().order_by('id')  # You forgot this line!
        
        category = self.kwargs.get('category')
        difficulty = self.kwargs.get('difficulty')
        
        if category:
            queryset = queryset.filter(category=category)
        if difficulty:
            queryset = queryset.filter(difficulty=difficulty)
        
        return queryset 

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all().order_by('id')
    serializer_class = QuestionSerializer

# User views
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer