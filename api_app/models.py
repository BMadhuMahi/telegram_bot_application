
from django.contrib.auth.models import User
from django.db import models

class TelegramProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    telegram_username = models.CharField(max_length=255, unique=True)
