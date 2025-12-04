from rest_framework import serializers
from .models import Question, User

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question', 'answers', 'correct_answer', 'category', 'difficulty')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'user_name', 'time', 'points', 'difficulty', 'category')
