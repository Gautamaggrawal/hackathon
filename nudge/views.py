from rest_framework.authtoken import views as auth_views
from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import ManualSchema

from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import *
# class MyAuthToken(auth_views.ObtainAuthToken):
#     serializer_class = MyAuthTokenSerializer
#     if coreapi is not None and coreschema is not None:
#         schema = ManualSchema(
#             fields=[
#                 coreapi.Field(
#                     name="appName",
#                     required=True,
#                     location='form',
#                     schema=coreschema.String(
#                         title="appName",
#                         description="Valid appName for authentication",
#                     ),
#                 ),
#             ],
#             encoding="application/json",
#         )


# obtain_auth_token = MyAuthToken.as_view()



# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated  # <-- Here


# class HelloView(APIView):
#     permission_classes = (IsAuthenticated,)             # <-- And here

#     def get(self, request):
#         content = {'message': 'Hello, World!'}
#         return Response(content)


from django.shortcuts import render
from rest_framework import viewsets
# from .permissions import *
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer