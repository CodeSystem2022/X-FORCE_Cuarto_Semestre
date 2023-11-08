from django.db import models
from django.contrib.auth.models import User


class MyUser(models.Model):
    cbu = models.IntegerField(null=True, blank=True)
    dark_mode = models.BooleanField(default=False, null=True, blank=True)
    profile_photo = models.TextField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)