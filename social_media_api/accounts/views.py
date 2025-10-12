from rest_framework import generics, status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from .models import User as CustomUser
from .serializers import (
    UserSerializer,
    UserRegisterSerializer,
    LoginSerializer,
    UserProfileSerializer,
)


# Register View
class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer


# Login View
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


# Profile View
class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


# User ViewSet (for listing and viewing all users)
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()  
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


# Follow User View
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow_user(request, user_id):
    target_user = get_object_or_404(CustomUser, id=user_id)

    if target_user == request.user:
        return Response(
            {"detail": "You cannot follow yourself."},
            status=status.HTTP_400_BAD_REQUEST
        )

    request.user.following.add(target_user)
    return Response(
        {"detail": f"You are now following {target_user.username}."},
        status=status.HTTP_200_OK
    )


# Unfollow User View
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unfollow_user(request, user_id):
    target_user = get_object_or_404(CustomUser, id=user_id)

    if target_user == request.user:
        return Response(
            {"detail": "You cannot unfollow yourself."},
            status=status.HTTP_400_BAD_REQUEST
        )

    request.user.following.remove(target_user)
    return Response(
        {"detail": f"You have unfollowed {target_user.username}."},
        status=status.HTTP_200_OK
    )
