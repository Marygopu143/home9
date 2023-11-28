# views.py
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from security.models import User

def unsafe_users(request, user_id):
    """Fixed to prevent SQL injection"""

    try:
        # Attempt to convert user_id to an integer
        user_id = int(user_id)
        user = get_object_or_404(User, id=user_id)
        return HttpResponse(user)
    except ValueError:
        # Return a 404 response if user_id is not a valid integer
        raise Http404("Invalid user ID")
