# Create your views here.
from django.shortcuts import render, redirect
from .forms import NewUserForm,UploadForm
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from django.http import HttpResponse

def homepage(request):
	return render(request=request, template_name='testapp/home.html')
def headerpage(request):
	return render(request=request, template_name='testapp/header.html')
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful.")
			return redirect("/header")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="testapp/register.html", context={"register_form":form})
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/header")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="testapp/login.html", context={"login_form":form})

from testapp.functions.functions import handle_uploaded_file
#from testapp.forms import UploadForm
def uploads(request):
    if request.method == 'POST':
        upload = UploadForm(request.POST, request.FILES)
        if upload.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File uploaded successfuly")

    else:
        upload = UploadForm()
        return render(request,"testapp/upload.html",{'form':upload})