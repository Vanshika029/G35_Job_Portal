
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate, login as auth_login 
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Job, Wishlist, Contact, Register, JobPost, ProfessionalDetails, AppliedJob  
from .forms import JobForm, JobPostForm  
from datetime import datetime

def home(request):
    return render(request, 'index.html')  # Main page

# def home_view(request):
#     # Render the main page template
#     return render(request, 'index.html')

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})

@login_required
def add_to_wishlist(request, job_id):
    job = Job.objects.get(id=job_id)
    priority = request.POST.get('priority', 'BP')  
    Wishlist.objects.create(user=request.user, job=job, priority=priority)
    messages.success(request, f"{job.title} added to your wishlist!")
    return redirect('job_list')

@login_required
def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user).order_by('priority', 'added_on')
    for item in wishlist_items:
        days_left = (item.job.deadline - datetime.now().date()).days
        if item.priority == 'HP' and days_left <= 3:
            messages.warning(request, f"Deadline for {item.job.title} is nearing ({days_left} days left)!")
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})

# Job category views
def itjobs(request):
    # jobs = Job.objects.all()  # Fetch all jobs from the database
    return render(request, 'itjobs.html')

def sales(request):
    return render(request, 'sales.html')

def marketing(request):
    return render(request, 'marketing.html')

def data(request):
    return render(request, 'data.html')

def hr(request):
    return render(request, 'hr.html')

def engineering(request):
    return render(request, 'engineering.html')

# Jobs in demand views
def fresher(request):
    return render(request, 'fresher.html')
def fresher1(request):
    return render(request, 'fresher1.html')

def fresher2(request):
    return render(request, 'fresher2.html')

def mnc(request):
    return render(request, 'mnc.html')

def mnc1(request):
    return render(request, 'mnc1.html')

def mnc2(request):
    return render(request, 'mnc2.html')

def remote(request):
    return render(request, 'remote.html')

def work(request):
    return render(request, 'work.html')

def walk(request):
    return render(request, 'walk.html')

def part(request):
    return render(request, 'part.html')

# Jobs by location views
def delhi(request):
    return render(request, 'delhi.html')

def mumbai(request):
    return render(request, 'mumbai.html')

def banglore(request):  
    return render(request, 'banglore.html')

def hyderabad(request):
    return render(request, 'hyderabad.html')

def chennai(request):
    return render(request, 'chennai.html')

def pune(request):
    return render(request, 'pune.html')

def details(request):
    return render(request, 'details.html')  

def it1(request):
    return render(request, 'it1.html')

def it2(request):
    return render(request, 'it2.html')
def sales(request):
    return render(request, 'sales.html')  # Ensure 'sales.html' uses {% static %} for static files

def sales1(request):
    return render(request, 'sales1.html')  # Ensure 'sales1.html' uses {% static %} for static files
def sales2(request):
    return render(request, 'sales2.html') 



# Other pages
def join(request):
    if not request.user.is_authenticated:
        messages.error(request, "You need to log in to access this page.")
        return redirect('login')

    if request.method == 'POST':
        company = request.POST.get('company')
        job_title = request.POST.get('job_title')
        salary = request.POST.get('salary')
        location = request.POST.get('location')

        # Save the job post to the JobPost model
        JobPost.objects.create(
            company=company,
            job_title=job_title,
            salary=salary,
            location=location
        )
        
        messages.success(request, "Job posted successfully!")
        return redirect('home')

    return render(request, 'join.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if not all([name, email, message]):
            messages.error(request, "All fields are required.")
            return render(request, 'contact.html')

        # Save the contact form data to the database
        contact = Contact(name=name, email=email, message=message)
        contact.save()

        messages.success(request, "Thank you for your message! We will get back to you soon.")
        return redirect('home')

    return render(request, 'contact.html')

@login_required
@user_passes_test(lambda u: u.is_staff)
def dashboard(request):
    job_posts = JobPost.objects.all()  # Ensure JobPost model is used
    return render(request, 'dashboard.html', {'job_posts': job_posts})

@login_required
@user_passes_test(lambda u: u.is_staff)
def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = JobForm()
    return render(request, 'create_job.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def update_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = JobForm(instance=job)
    return render(request, 'update_job.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST':
        job.delete()
        return redirect('dashboard')
    return render(request, 'delete_job.html', {'job': job})

@login_required
@user_passes_test(lambda u: u.is_staff)
def create_job_post(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Job post created successfully!")
            return redirect('dashboard') 
    else:
        form = JobPostForm()
    return render(request, 'create_job_post.html', {'form': form})

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        messages.success(request, "You have been logged out successfully.")
    return redirect('login')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')  
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile', '') 
        role = request.POST.get('role', '')     

       
        full_name = username

       
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists in User model.")
            return redirect('register')
        if Register.objects.filter(email=email).exists():
            messages.error(request, "Email already exists in Register model.")
            return redirect('register')

        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        
        register = Register(full_name=full_name, email=email, mobile=mobile, role=role)
        register.save()

        
        messages.success(request, "Registration successful! You can now log in.")
        return redirect('login')

    return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, f"Welcome! {user.first_name}!")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials.")
    return render(request, 'login.html')

# Company-specific views
def tesla(request):
    return render(request, 'tesla.html')

def meta(request):
    return render(request, 'meta.html')

def netflix(request):
    return render(request, 'netflix.html')


@login_required
def dashboard(request):
    job_posts = JobPost.objects.all()  
    return render(request, 'dashboard.html', {'job_posts': job_posts})

def delete_job(request, job_id):
    job_post = get_object_or_404(JobPost, id=job_id) 
    if request.method == 'POST':
        job_post.delete()
        messages.success(request, "Job deleted successfully!")
        return redirect('dashboard')
    return render(request, 'delete_job.html', {'job': job_post})

def update_job(request, job_id):
    job_post = get_object_or_404(JobPost, id=job_id)  
    if request.method == 'POST':
        job_post.company = request.POST['company']
        job_post.job_title = request.POST['job_title']
        job_post.salary = request.POST['salary']
        job_post.location = request.POST['location']
        job_post.save()
        messages.success(request, "Job updated successfully!")
        return redirect('dashboard')
    else:
        
        return render(request, 'update_job.html', {'job': job_post})

@login_required
def submit_professional_details(request):
    if request.method == 'POST':
        designation = request.POST.get('designation')
        company = request.POST.get('company')
        experience = request.POST.get('experience')
        skills = request.POST.get('skills')
        tenth_marks = request.POST.get('tenth_marks')
        twelfth_marks = request.POST.get('twelfth_marks')
        graduation_degree = request.POST.get('graduation_degree')
        graduation_institute = request.POST.get('graduation_institute')
        graduation_year = request.POST.get('graduation_year')
        location = request.POST.get('location')

       
        ProfessionalDetails.objects.update_or_create(
            user=request.user,
            defaults={
                'designation': designation,
                'company': company,
                'experience': experience,
                'skills': skills,
                'tenth_marks': tenth_marks,
                'twelfth_marks': twelfth_marks,
                'graduation_degree': graduation_degree,
                'graduation_institute': graduation_institute,
                'graduation_year': graduation_year,
                'location': location,
            }
        )
        messages.success(request, "Professional details submitted successfully!")
        return redirect('home')  
    return render(request, 'details.html')  

@login_required
def professional_details_dashboard(request):
    details = ProfessionalDetails.objects.filter(user=request.user)  # Filter details for the logged-in user
    return render(request, 'professional_details_dashboard.html', {'details': details})

@login_required
def update_professional_details(request, detail_id):
    detail = get_object_or_404(ProfessionalDetails, id=detail_id)
    if request.method == 'POST':
        detail.designation = request.POST.get('designation')
        detail.company = request.POST.get('company')
        detail.experience = request.POST.get('experience')
        detail.skills = request.POST.get('skills')
        detail.tenth_marks = request.POST.get('tenth_marks')
        detail.twelfth_marks = request.POST.get('twelfth_marks')
        detail.graduation_degree = request.POST.get('graduation_degree')
        detail.graduation_institute = request.POST.get('graduation_institute')
        detail.graduation_year = request.POST.get('graduation_year')
        detail.location = request.POST.get('location')
        detail.save()
        messages.success(request, "Professional details updated successfully!")
        return redirect('professional_details_dashboard')
    return render(request, 'update_professional_details.html', {'detail': detail})

@login_required
def delete_professional_details(request, detail_id):
    detail = get_object_or_404(ProfessionalDetails, id=detail_id)
    if request.method == 'POST':
        detail.delete()
        messages.success(request, "Professional details deleted successfully!")
        return redirect('professional_details_dashboard')
    return render(request, 'delete_professional_details.html', {'detail': detail})

@login_required
def apply(request):
    if request.method == 'POST':
        job_title = request.POST.get('job_title', 'Unknown Job')
        company = request.POST.get('company', 'Unknown Company')

        # Check if the job is already applied for by the user
        if not AppliedJob.objects.filter(user=request.user, job_title=job_title, company=company).exists():
            # Save the applied job to the database
            AppliedJob.objects.create(user=request.user, job_title=job_title, company=company)
            messages.success(request, f"You have successfully applied for {job_title} at {company}.")
        else:
            messages.info(request, f"You have already applied for {job_title} at {company}.")

        # return redirect('applied_jobs')  # Redirect to the applied jobs page

    return render(request, 'apply.html')

@login_required
def applied_jobs(request):
    # Fetch all applied jobs for the logged-in user
    applied_jobs = AppliedJob.objects.filter(user=request.user).order_by('-applied_at')
    return render(request, 'applied_jobs.html', {'applied_jobs': applied_jobs})

def job_list(request):
    jobs = Job.objects.all()  # Fetch all job objects
    return render(request, 'index/templates/apply.html', {'jobs': jobs})

@login_required(login_url='/login/')  # Redirect to login page if not authenticated
def applied_jobs(request):
    applied_jobs = Job.objects.filter(wishlist__user=request.user)  # Example logic
    return render(request, 'applied_jobs.html', {'applied_jobs': applied_jobs})
