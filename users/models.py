from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Theme(models.TextChoices):
        DARK = 'Темная'
        LIGHT = 'Светлая'


    avatar = models.ImageField(blank=True, upload_to='users_images')
    preferred_theme = models.CharField(choices=Theme.choices, default=Theme.LIGHT, max_length=10)
