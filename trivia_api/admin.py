from django.contrib import admin
from .models import Question, User

# Register models
admin.site.register(Question)
admin.site.register(User)
