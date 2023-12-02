# import json
# from django.http import HttpResponse, JsonResponse
# from rest_framework import generics
# from .models import User, UserRole
# from .serializers import UserSerializer, UserRoleSerializer
# from django.views import View

# class UserRoleList(generics.ListCreateAPIView):
#     queryset = UserRole.objects.all()
#     serializer_class = UserRoleSerializer

# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserRoleList(View):
#     def get(self, request):
#         user_roles = UserRole.objects.all()
#         return JsonResponse({'user_roles': list(user_roles.values())})
    
#     def post(self, request):
#         data = json.loads(request.body)
#         role_name = data.get('name', None)
#         if role_name is not None:
#             new_role = UserRole.objects.create(name=role_name)
#             return JsonResponse({'id': new_role.id, 'name': new_role.name})
#         else:
#             return HttpResponse('Bad Request: Missing role name', status=400)
from rest_framework import viewsets
from .models import UserRole
from .serializers import UserRoleSerializer

class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer
    
    def save(self, *args, **kwargs):
        self.role = self.role.title()
        super(UserRole, self).save(*args, **kwargs)