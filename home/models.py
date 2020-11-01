from django.db import models
from django.contrib.auth.models import User


class Passwords(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    website_url = models.TextField()
    website_name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=256)
    keys = models.TextField(blank=True, null=True)
