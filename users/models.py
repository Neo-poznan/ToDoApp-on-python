from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    avatar = models.ImageField(blank=True, upload_to='users_images')
    preferred_theme_is_dark = models.BooleanField(default=False)
