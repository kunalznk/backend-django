from rest_framework import generics
from rest_framework.response import Response
from .serializer import UserSerializer
from .models import User
class UserCreateApi(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserApi(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDeleteApi(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer