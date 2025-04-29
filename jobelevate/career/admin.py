from django.contrib import admin
from .models import CareerPost

class CareerPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'content')

admin.site.register(CareerPost, CareerPostAdmin)