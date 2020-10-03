from django.urls import path
from . views import UserList

app_name = 'users'

urlpatterns = [
    path('user-list', UserList.as_view(), name='user-list'),
]
