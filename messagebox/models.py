from django.db import models

class Message(models.Model):
    title = models.CharField(max_length=40)
    text = models.TextField()

