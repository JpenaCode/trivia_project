from django.shortcuts import render
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
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
    serializer_class = UserSerializer
    
    def get_queryset(self):
        """Handle GET requests - optionally filter by user_name"""
        queryset = User.objects.all().order_by('-id')
        
        user_name = self.request.query_params.get('user_name')
        if user_name:
            queryset = queryset.filter(user_name=user_name)
        
        return queryset
    
    def create(self, request, *args, **kwargs):
        """Handle POST requests - always create a new record"""
        # Extract query parameters
        user_name = request.query_params.get('user_name', '').strip()
        category = request.query_params.get('category', '').strip()
        difficulty = request.query_params.get('difficulty', '').strip()
        
        # Validate required parameters
        if not user_name:
            raise ValidationError({
                "user_name": "This query parameter is required and cannot be empty."
            })
        
        # Create new user record
        user = User.objects.create(
            user_name=user_name,
            category=category,
            difficulty=difficulty,
            time=timezone.now(),
            points=0
        )
        
        # Serialize and return the created user
        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
# class UserList(generics.ListCreateAPIView):
#     # queryset = User.objects.all().order_by('id')
#     serializer_class = UserSerializer
    
#     def no_user_response(self):
#         print("provide a user")
#         raise ValidationError({"user_name": "This query parameter is required."})
        
#     def get_queryset(self):
#         queryset = User.objects.all().order_by('id')
#         params = self.request.query_params
        
#         if "user_name" not in params:
#             print("provide a user_name")
#             raise ValidationError({"user_name": "Please include the user_name param in the url"})
#         elif len(params.get("user_name")) == 0:
#             raise ValidationError({"user_name": "Please send a user_name through"})
#         else:
#             user_name = self.request.query_params.get('user_name')
        
#             # Use get_or_create - creates if doesn't exist, returns existing if it does
#             user, created = User.objects.get_or_create(
#                 user_name=user_name,
#                 defaults={
#                     'time': timezone.now(),  # Import: from django.utils import timezone
#                     'points': 0,
#                     'difficulty': '',
#                     'category': ''
#                 }
#             )
        
#             if created:
#                 print(f"New user created: {user}")
#             else:
#                 print(f"User already exists: {user}")
            
#             # Return only this user's records
#             queryset = queryset.filter(user_name=user_name)
        
#         return queryset 

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        
        # Priority: query params override body data
        update_data = {}
        
        # Get from query params first
        if request.query_params.get('category'):
            update_data['category'] = request.query_params.get('category')
        if request.query_params.get('difficulty'):
            update_data['difficulty'] = request.query_params.get('difficulty')
        if request.query_params.get('points'):
            update_data['points'] = int(request.query_params.get('points'))
        
        # Merge with body data (query params take precedence)
        body_data = request.data.copy() if request.data else {}
        body_data.update(update_data)
        
        # Always update time
        body_data['time'] = timezone.now()
        
        # Use serializer for validation
        serializer = self.get_serializer(instance, data=body_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data)

