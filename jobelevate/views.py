from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  # For displaying success messages
from .models import Job  # Assuming Job is the model for job postings
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def dashboard(request):
    jobs = Job.objects.all()  # Fetch all job postings
    context = {
        'jobs': jobs,
        'user': request.user,
        'has_submitted_details': request.user.profile.has_submitted_details,  # Assuming a profile model
    }
    return render(request, 'dashboard.html', context)  # Add render call to return response

# def job_list(request):
#     jobs = Job.objects.all()  # Fetch all job objects
#     return render(request, 'index/templates/apply.html', {'jobs': jobs})
