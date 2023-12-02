from rest_framework import serializers
from .models import User, UserRole

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = ['id', 'role']

class UserSerializer(serializers.ModelSerializer):
    user_role = UserRoleSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'pincode', 'mobile', 'user_role', 'status']