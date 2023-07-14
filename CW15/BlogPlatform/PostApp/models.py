from django.db import models
from AuthorApp.models import Author

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=64)
    subject = models.CharField(max_length=128)
    content = models.TextField()
    publish_date = models.DateField(auto_now_add= True)
    update_date = models.DateField(auto_now=True)


    def __str__(self) -> str:
        text = f"Title: {self.name}\nSubject: {self.subject}\nContent: {self.bio}\Created at: {self.Creation_date}\n"
        return text


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add= True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        text = f"Name: {self.name}\nEmail: {self.email}\nPost: {self.post}\nMessage: {self.message}\nCreated at: {self.created_date}"
        return text