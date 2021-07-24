# from django.urls import path, include
# from rest_framework.authtoken.views import obtain_auth_token
# from nudge import views
# from rest_framework import routers
# # from userapi.views import UserViewSet

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)

# urlpatterns = [
#     #other paths
#     path(r'', include(router.urls)),
#     path('api-token-auth/', views.obtain_auth_token, name='api_token_auth'),
# ]

# urlpatterns = [
#     path('hello/', views.HelloView.as_view(), name='hello'),
#     path('api-token-auth/', views.obtain_auth_token, name='api_token_auth'),
# ]

# from rest_framework import routers
# from userapi.views import UserViewSet

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

# urlpatterns = [
#     #other paths
#     path(r'', include(router.urls)),
#     path(r'api-token-auth/', obtain_jwt_token),
#     path(r'api-token-refresh/', refresh_jwt_token),
#     path(r'api-token-verify/', verify_jwt_token),
# ]
from django.urls import path, include
from rest_framework import routers
from nudge.views import UserViewSet
from django.urls import path, include

router = routers.DefaultRouter()

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("api/<version>/", include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]