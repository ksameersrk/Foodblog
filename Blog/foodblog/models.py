from django.db import models
from django.utils import timezone
from django import forms

class Post(models.Model):
    author = models.TextField()
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Auth(models.Model):
    username = models.TextField()
    password = models.TextField(default='xxxx')
    email = models.TextField(default='asdf@xyz.com')
    phone = models.IntegerField(default='888888888')

    def __str__(self):
        return self.username