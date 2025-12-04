from django.urls import path
from . import views

urlpatterns = [
    path('api/questions', views.QuestionList.as_view(), name='question_list'),
    path('api/questions/<int:pk>', views.QuestionDetail.as_view(), name='question_detail'),
	path('api/users', views.UserList.as_view(), name='user_list'),
	path('api/users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
]
