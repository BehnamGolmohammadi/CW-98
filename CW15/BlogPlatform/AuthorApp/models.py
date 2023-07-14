from django.db import models

# Create your models here.
def user_img_directory(instance, filename):
    return "Author_image/user_%s/%s" %(instance, filename)

class Author(models.Model):
    name = models.CharField(max_length=32)
    bio = models.CharField(max_length=256)
    image = models.ImageField(upload_to=user_img_directory)
    register_date = models.DateField(auto_now_add= True)

    def __str__(self) -> str:
        text = f"Name: {self.name}\nBiography: {self.bio}\Registerd at: {self.register_date}\n"
        return text