from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True,blank=True)
    profil_photo = models.ImageField(upload_to='profilPhoto/',blank = True)
