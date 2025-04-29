from django.shortcuts import render

# Create your views here.
from .models import CareerPost


from .models import CareerInterest
from .forms import CareerInterestForm

def career_tips(request):
    posts = CareerPost.objects.all().order_by('-created_at')
    return render(request, 'career_tips.html', {'posts': posts})

def prepare_for_interview(request):
    return render(request, 'interview.html')

def skills(request):
    return render(request, 'skill.html')




def career_roadmap_view(request):
    selected_career = None
    if request.method == 'POST':
        form = CareerInterestForm(request.POST)
        if form.is_valid():
            selected_career = form.cleaned_data['interest']
    else:
        form = CareerInterestForm()

    return render(request, 'career_roadmap.html', {'form': form, 'career': selected_career})