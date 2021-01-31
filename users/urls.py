from django.urls import path

from users.views import UserList
from users.views import CurrentUserRetrieveUpdateView
from users.views import auth_token


urlpatterns_users = [
    path('auth/register/', UserList.as_view(), name='UserList'),  # local item url created
    path('auth/login/', auth_token),
    path('current/', CurrentUserRetrieveUpdateView.as_view(), name='CurrentUser'),
]
