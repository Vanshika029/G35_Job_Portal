from django.urls import path
from . import views


urlpatterns = [
    path('career-tips/', views.career_tips, name='career_tips'),  # Add this route
    path('prepare-for-interview/', views.prepare_for_interview, name='interview'),
    # path('skills/', views.skills, name='skills'),  # Add this route
    path('skill/', views.skills, name='skill'),  
    path('roadmap/', views.career_roadmap_view, name='career_roadmap'),]
