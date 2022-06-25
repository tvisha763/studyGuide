from django.db import models
from django.forms import CharField
from django.utils import timezone

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=10, default='')
    password = models.CharField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    salt = models.CharField(max_length=1023)
    def __str__(self):
        return '%s - %s' % (self.username, self.email)

class Post(models.Model):
    POST_CHOICES = [
        (1, 'None'),
        (2, 'Sale'),
        (3, 'Practice'),
        (4, 'Tutoring')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to="saleImgs")
    description = models.CharField(max_length=500, blank=True)
    postType = models.IntegerField(default=1, choices=POST_CHOICES)
    date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(blank=True, null=True)
    sale = models.JSONField(blank=True, null=True)
    practice = models.JSONField(blank=True, null=True)
    tutor = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.user.username}'