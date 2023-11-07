from django.db import models
from django.contrib.auth.models import User

# Create a model named 'UploadedFile' to represent uploaded files
class UploadedFile(models.Model):
    # Associate each file with a user using a foreign key
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Store the uploaded file using the 'FileField' with a directory specified by 'upload_to'
    file = models.FileField(upload_to='uploads/')
    # Store the name of the file
    file_name = models.CharField(max_length=255)
    # Store the size of the file as a positive integer
    file_size = models.PositiveIntegerField(default=0)
    # Track the upload progress as a positive integer (default to 0)
    upload_progress = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.file_name
