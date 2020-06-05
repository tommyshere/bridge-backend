from rest_framework import generics
from .models import SignUp
from .serializers import SignUpSerializer


class SignUp(generics.CreateAPIView):
    queryset = SignUp.objects.all()
    serializer_class = SignUpSerializer
