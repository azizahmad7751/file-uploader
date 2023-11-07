from django.contrib import admin
from .models import UploadedFile

@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('user', 'file_name', 'file_size', 'upload_progress')
    list_filter = ('user',)
    search_fields = ('user__username', 'file_name')

