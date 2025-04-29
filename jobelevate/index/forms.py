from django import forms
from .models import Job, JobPost

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'location', 'company']

class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = ['company', 'job_title', 'salary', 'location']
