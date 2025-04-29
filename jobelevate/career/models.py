from django.db import models

# Create your models here.
class CareerPost(models.Model):
    CATEGORY_CHOICES = [
        ('resume', 'Resume Tips'),
        ('interview', 'Interview Tips'),
        ('networking', 'Networking Tips'),
        ('career_growth', 'Career Growth'),
    ]
    
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='resume')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title






class CareerInterest(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class CareerStep(models.Model):
    career = models.ForeignKey(CareerInterest, related_name='steps', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['order']  # Steps will appear in correct order

    def __str__(self):
        return f"{self.career.name} - Step {self.order}: {self.title}"