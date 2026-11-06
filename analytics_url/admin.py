from django.contrib import admin
from .models import ShortenedURL

# Register your models here.
@admin.register(ShortenedURL)
class ShortenedURLAdmin(admin.ModelAdmin):
    list_display = ('short_code', 'original_url', 'clicks', 'created_at')