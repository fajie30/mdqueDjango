# from django.urls import path
# from .views import UserList, UserRoleList

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserRoleViewSet

router = DefaultRouter()
router.register(r'user_roles', UserRoleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = [
#     path('user_roles/', UserRoleList.as_view()),
#     path('users/', UserList.as_view()),
# ]