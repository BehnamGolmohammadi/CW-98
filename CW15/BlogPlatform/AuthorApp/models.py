from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=32)
    bio = models.CharField(max_length=256)
    register_date = models.DateField(auto_now_add= True)

    def __str__(self) -> str:
        text = f"Name: {self.name}\nBiography: {self.bio}\Registerd at: {self.register_date}\n"
        return text