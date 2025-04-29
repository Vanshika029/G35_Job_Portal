from django.urls import path, include  
from . import views
from django.contrib.auth.decorators import user_passes_test, login_required

# Check if the user is an admin
def is_admin(user):
    return user.is_authenticated and user.is_staff  

urlpatterns = [
    path('', views.home, name='home'),  # Main page
    path('index/', views.home, name='index'),  # Add or uncomment this line for the 'index' URL
    path('jobs/', views.job_list, name='job_list'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add-to-wishlist/<int:job_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    # Job categories
    path('itjobs/', views.itjobs, name='itjobs'),
    path('it1/', views.it1, name='it1'),
    path('it2/', views.it2, name='it2'),
    path('sales/', views.sales, name='sales'),
    path('marketing/', views.marketing, name='marketing'),
    path('data/', views.data, name='data'),
    path('hr/', views.hr, name='hr'),
    path('engineering/', views.engineering, name='engineering'),
    # Jobs in demand
    path('fresher/', views.fresher, name='fresher'),
    path('fresher1/', views.fresher1, name='fresher1'),
    path('fresher2/', views.fresher2, name='fresher2'),
    path('sales/', views.sales, name='sales'),
    path('sales1/', views.sales1, name='sales1'),
    path('sales2/', views.sales2, name='sales2'),

    path('mnc/', views.mnc, name='mnc'),
    path('mnc1/', views.mnc1, name='mnc1'),
    path('mnc2/', views.mnc2, name='mnc2'),
    path('remote/', views.remote, name='remote'),
    path('work/', views.work, name='work'),
    path('walk/', views.walk, name='walk'),
    path('part/', views.part, name='part'),
    # Jobs by location
    path('delhi/', views.delhi, name='delhi'),
    path('mumbai/', views.mumbai, name='mumbai'),
    path('banglore/', views.banglore, name='banglore'),  
    path('hyderabad/', views.hyderabad, name='hyderabad'),
    path('chennai/', views.chennai, name='chennai'),
    path('pune/', views.pune, name='pune'),
    # Other pages
    
    path('contact/', views.contact, name='contact'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),  # Ensure this URL is defined
    path('join/', views.join, name='join'),
    path('dashboard/', views.dashboard, name='dashboard'),  
    path('update-job/<int:job_id>/', views.update_job, name='update_job'), 
    path('delete-job/<int:job_id>/', views.delete_job, name='delete_job'),  
    path('details/', views.details, name='details'),  
    path('submit-professional-details/', login_required(views.submit_professional_details), name='submit_professional_details'),  
    path('professional-details-dashboard/', login_required(views.professional_details_dashboard), name='professional_details_dashboard'),
    path('update-professional-details/<int:detail_id>/', views.update_professional_details, name='update_professional_details'),
    path('delete-professional-details/<int:detail_id>/', views.delete_professional_details, name='delete_professional_details'),

    # Company-specific
    path('tesla/', views.tesla, name='tesla'),
    path('meta/', views.meta, name='meta'),
    path('netflix/', views.netflix, name='netflix'),

    path('apply/', views.apply, name='apply'),
    path('apply/<int:job_id>/', views.apply, name='apply'),  # Example apply URL
    path('applied-jobs/', views.applied_jobs, name='applied_jobs'),
]