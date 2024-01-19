from django.utils import timezone
from django.db import models
from django.contrib.auth.hashers import make_password


class UserRole(models.Model):
    role = models.CharField(max_length=200)

    def __str__(self):
        return self.role

class User(models.Model):
    pincode = models.CharField(max_length=200)
    mobile = models.CharField(max_length=20)
    date_registered = models.DateTimeField(default=timezone.now)
    user_role = models.ForeignKey(UserRole, on_delete=models.CASCADE)
    status = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        self.pincode = make_password(self.pincode)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.mobile

