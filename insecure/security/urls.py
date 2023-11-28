# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Safe URL for users
    # http://127.0.0.1:8080/security/safe/users/1 or 1
    path('unsafe/users/<user_id>', views.unsafe_users, name='unsafe_users'),
]
