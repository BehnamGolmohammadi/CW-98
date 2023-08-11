from django.db import models
from django.db.models import Count

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.name}"

    def get_task_count(self):
        return self.task_set.count()