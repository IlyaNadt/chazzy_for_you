from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

class Message(models.Model):

    title = models.CharField(max_length=40)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True,unique_for_date='date')

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('messagebox:message_detail', args=[self.slug,])
    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.title[:50]
