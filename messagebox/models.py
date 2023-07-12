from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Message(models.Model):
    title = models.CharField(max_length=40)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.title[:50]
