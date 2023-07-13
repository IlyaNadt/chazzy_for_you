from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Message(models.Model):

    title = models.CharField(max_length=40)
    slug = models.SlugField(max_length=40, unique=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.title[:50]
