from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

def home(request):
    return JsonResponse({"message": "Welcome to the Social Media API!"})

@api_view(['GET'])
def api_overview(request):
    return Response({
        "register": "/api/accounts/register/",
        "login": "/api/accounts/login/",
        "profile": "/api/accounts/profile/",
    })