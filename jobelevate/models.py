from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    role = models.CharField(max_length=10, choices=[('user', 'User'), ('admin', 'Admin')])

    def __str__(self):
        return self.username

class JobPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add this field
    company = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    salary = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)

    def __str__(self):
        return self.title
