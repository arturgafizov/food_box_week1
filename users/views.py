from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

from users.models import User
from users.models import UserSerializer, UserCurrentSerializer


class UserList(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRegisterViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@ csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def auth_token(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=HTTP_200_OK)


class CurrentUserRetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class = UserCurrentSerializer

    def get_object(self):
        return self.request.user
