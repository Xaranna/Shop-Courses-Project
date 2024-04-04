from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='users_images', null=True, blank=True)