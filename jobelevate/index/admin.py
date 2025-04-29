from django.contrib import admin
from .models import JobPost, ProfessionalDetails  # Import the JobPost and ProfessionalDetails models

# Customize the JobPost admin interface
@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company', 'location', 'salary', 'location')  # Fields to display in the admin list view
    # search_fields = ('job_title', 'company', 'location')  # Fields to enable search functionality
    # list_filter = ('company', 'location', 'posted_on')  # Fields to enable filtering

admin.site.register(ProfessionalDetails)

