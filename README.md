# File Uploader

File Uploader is a Django web application that allows users to upload and manage files. It provides a user-friendly interface for uploading, downloading, and managing files.

## Features

- User registration and authentication.
- File upload with progress tracking.
- Download files that have been uploaded.
- Pause and resume file uploads.
- File management for each user.
- Easy-to-use web interface.

## Live Demo

You can try out the application with the live demo. Visit [File Uploader Demo](https://uploader7751.pythonanywhere.com/) and experience the features of the application without the need to set it up locally.



## Installation

```bash
# Clone the repository
https://github.com/azizahmad7751/file-uploader.git

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate

# On Windows, use
venv\Scripts\activate

# Install project dependencies
pip install -r requirements.txt

# Apply migrations to set up the database
python manage.py migrate

# Start the development server
python manage.py runserver

Access the application in your web browser at http://localhost:8000/.


##Usage
1. Register a new user or log in if you already have an account.

2. Click the "File Upload" button to upload a file. You can see the upload progress.

3. After uploading, you can view and download your uploaded files in the "DOWNLOAD" section.


