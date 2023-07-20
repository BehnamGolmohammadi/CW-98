from django.db import models

# Create your models here.
class Category:
    name = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.name}"
