from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, FileResponse
from .models import UploadedFile
import os
from django.core.files import File
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


def user_registration(request):
    if request.method == 'POST':
        # Handle user registration form submission
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Create a new user and login them 
            user = form.save()
            login(request, user)
            return redirect('user_login')
    else:
         # Display the registration form for GET requests
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        # Handle user login form submission
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Log the user in and redirect to the file upload page after successful login
            login(request, user)
            return redirect('upload_file')  # Redirect to the file upload page after successful login
            # Display the login form for GET requests or after a failed login attempt
  
    return render(request, 'login.html')



@login_required
def upload_file(request):
    print(f"Authenticated user: {request.user}")
    if request.method == 'POST':
        # Handle file upload
        uploaded_file = request.FILES['file']
        file_name = uploaded_file.name
        new_file = UploadedFile(user=request.user, file=uploaded_file, file_name=file_name)
        new_file.save()
        return render(request, 'index.html', {'uploaded_file': new_file})
    # Display the file upload form for GET requests    
    return render(request, 'index.html')

'''


@login_required
def upload_file(request):
    progress = 0  # Provide a default value for progress

    if request.method == 'POST':
        uploaded_file = request.FILES.get('file')
        if uploaded_file:
            # Calculate the total file size
            total_size = uploaded_file.size
            uploaded_size = 0

            # Get the file name from the uploaded file
            file_name = uploaded_file.name

            new_file = UploadedFile(user=request.user, file_name=file_name)
            new_file.file = uploaded_file  # Associate the file attribute
            new_file.save()

            with new_file.file.open('wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
                    uploaded_size += len(chunk)
                    progress = int((uploaded_size / total_size) * 100)
                    new_file.upload_progress = progress
                    new_file.save()

            progress = 100

    return render(request, 'index.html', {'progress': progress})
    '''

@login_required
def download_file(request, file_id):
    try:
        file = UploadedFile.objects.get(pk=file_id)
        file_path = file.file.path
        print(file_path)

        # Check if the file exists before opening and serving it
        if os.path.exists(file_path):
            response = FileResponse(open(file_path, 'rb'), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{file.file_name}"'
            return response
        else:
            raise Http404("File not found")
    except UploadedFile.DoesNotExist:
        raise Http404("File not found")
'''
@login_required
def get_upload_progress(request):
    if request.method == 'GET':
        file_id = request.GET.get('file_id', None)
        if file_id:
            file = UploadedFile.objects.get(id=file_id)
            file_size = os.path.getsize(file.file.path)
            return JsonResponse({'progress': file_size})
    return JsonResponse({'progress': 0})
'''
