from django.shortcuts import render
from . models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView

class UserList(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = User.objects.all()
        # return only active user => if active return else
        return queryset
# Create your views here.
