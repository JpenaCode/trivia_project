from django.shortcuts import render

from rest_framework import generics
from .models import Question, User
from .serializers import QuestionSerializer, UserSerializer

# Question views
class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all().order_by('id')
    serializer_class = QuestionSerializer
	# def get_queryset(self):
	# 	print("--- ContactList: Executing GET request. ---")
	# 	return super().get_queryset()

	# def post(self, request, *arg, **kwargs) :
	# 	print(f"--- ContactList: Executing POST request with data: {reques.data} ---")
	# 	return super().post(request, *args, **kwards)

	# def get_queryset(self):
	# 	# Print to confirm GET request reached here
	# 	print("--- ContactList: Executing GET request. ---")
	# 	return super().get_queryset()
	# def post(self, request, *args, **kwargs):
	# 	# Print to confirm POST request reached here, and show incoming data
	# 	print(f"--- ContactList: Executing POST request with data: {request.data} ---")
	# 	return super().post(request, *args, **kwargs)

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
