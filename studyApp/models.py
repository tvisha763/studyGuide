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
        (1, 'Sale'),
        (2, 'Practice'),
        (3, 'Tutoring')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    postType = models.IntegerField(default=1, choices=POST_CHOICES)
    materialName = models.CharField(max_length=100, unique=False, blank=True, default='')
    image = models.ImageField(upload_to="uploads", blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    pracFile = models.FileField(upload_to="uploads", blank=True)
    subjectPrac = models.CharField(max_length=100, blank=True)
    fname =  models.CharField(max_length=100, blank=True, default='')
    lname =  models.CharField(max_length=100, blank=True, default='')
    subjectsTutor = models.CharField(max_length=1000, blank=True)
    rate = models.IntegerField(default=0, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.id}{self.postType} - {self.user.username}'

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_likes")
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post} - {self.user}'

class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="peers")
    fname =  models.CharField(max_length=100, blank=True, default='')
    lname =  models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return f'{self.fname} - {self.user}'