from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to='Users/')

    def __str__(self) -> str:
        return f"#{self.pk} | {self.get_full_name()}"