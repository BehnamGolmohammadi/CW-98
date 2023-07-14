from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)

    def __str__(self) -> str:
        string = f"Name: {self.name}\nDescription: {self.description}"
        return string