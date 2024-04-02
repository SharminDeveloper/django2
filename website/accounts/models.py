from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
# Create your models here.
class CustomUserModel(AbstractUser):
    age = models.PositiveIntegerField(null = True , blank = True , validators=[MaxValueValidator(limit_value=100)])
    email = models.EmailField(unique=True, blank=False)