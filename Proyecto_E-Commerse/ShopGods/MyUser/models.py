from django.db import models
from django.contrib.auth.models import User


class MyUser(models.Model):
    client_id = models.CharField(max_length=255, null=True, blank=True)
    secret_key = models.CharField(max_length=255, null=True, blank=True)
    dark_mode = models.BooleanField(default=False, null=True, blank=True)
    profile_photo = models.TextField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
