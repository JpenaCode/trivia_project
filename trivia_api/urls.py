from django.urls import path
from . import views

urlpatterns = [
    path('api/questions', views.QuestionList.as_view(), name='question_list'),
    path('api/questions/<int:pk>', views.QuestionDetail.as_view(), name='question_detail'),
]
