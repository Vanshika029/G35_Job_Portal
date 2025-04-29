from django.db import models
from django.contrib.auth.models import User


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     mobile = models.CharField(max_length=15)
#     role = models.CharField(max_length=10, choices=[('user', 'User'), ('admin', 'Admin')])

#     def __str__(self):
#         return f"{self.user.username}'s profile" 
    

    
class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Wishlist(models.Model):
    PRIORITY_CHOICES = [
        ('HP', 'High Priority'),
        ('DJ', 'Dream Job'),
        ('BP', 'Backup Plan'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    priority = models.CharField(max_length=2, choices=PRIORITY_CHOICES, default='BP')
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.job.title}"
    


class JobPost(models.Model):
    # company = models.CharField(max_length=255,default="Unknown")
    company = models.CharField(max_length=255, null=False,default="Unknown")
    job_title = models.CharField(max_length=255 ,default="Default Job Title")
    # job_title = models.CharField(max_length=255, null=False,default="Default Job Title")
    salary = models.CharField(max_length=100 ,default="0")
    # salary = models.CharField(max_length=100, null=False,default="0") 
    location = models.CharField(max_length=255 ,default="Default Location")
    # location = models.CharField(max_length=255, null=False,default="Default Location")
    # created_at = models.DateTimeField(auto_now_add=True ) 

    def __str__(self):
        return f"{self.job_title} at {self.company}"


class Register(models.Model):
    ROLE_CHOICES = [
        ('user', 'User'),
        ('admin', 'Admin'),
    ]
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    mobile = models.CharField(max_length=15)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES,default='user')

    def __str__(self):
        return f"{self.full_name} ({self.role})"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Contact from {self.name} ({self.email})"

class ProfessionalDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    experience = models.IntegerField()
    skills = models.TextField()
    tenth_marks = models.FloatField()
    twelfth_marks = models.FloatField()
    graduation_degree = models.CharField(max_length=255)
    graduation_institute = models.CharField(max_length=255)
    graduation_year = models.IntegerField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username}'s Professional Details"

class AppliedJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.job_title} at {self.company} by {self.user.username}"


# class JobApplication(models.Model):
#     full_name = models.CharField(max_length=100)
#     email = models.EmailField()
#     resume = models.FileField(upload_to='resumes/')
#     cover_letter = models.TextField(blank=True)
#     job_title = models.CharField(max_length=100)
#     company = models.CharField(max_length=100)
#     applied_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.full_name} - {self.job_title}"