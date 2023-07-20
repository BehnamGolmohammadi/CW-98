from django.db import models
from CategoryApp.models import Category

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return f"{self.name}"



class Task(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    due_date = models.DateTimeField()
    status_choices = (('Todo','Todo'), ('Done','Done'), ('Doing','Doing'))
    status = models.CharField(max_length=5, choices=status_choices)
    tag = models.ManyToManyField(Tag)
    category = models.ManyToManyField(Category)

    def __str__(self) -> str:
        return f"{self.title} | {self.due_date} | {self.status}"
    