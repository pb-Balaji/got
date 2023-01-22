from django.shortcuts import  render, redirect
from .forms import NewUserForm,EnquiryForm
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from django.http import HttpResponseRedirect
from .models import Enquiry

def index(request):

     return render(request,'auth/index.html')

def login_view(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="auth/login.html", context={"login_form":form,'title':"Login page"})
    
def register_view(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="auth/register.html", context={"register_form":form ,"title":"Register page"})



def logout_view(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect('index')

def services(request):
	return render(request,'auth/services.html')

def about(request):
	return render(request,'auth/about.html')

def contact(request):
	return render(request,'auth/contact.html')

def team(request):
	return render(request,'auth/team.html')


def features(request):
	return render(request,'auth/features.html')


def enquiry(request):
	if request.method =="POST":
		name =request.POST.get('name')
		email =request.POST.get('email')
		subject =request.POST.get('subject')
		message =request.POST.get('message')
		data=Enquiry(name=name,email=email,subject=subject,message=message)
		data.save()
	return render(request,'auth/contact.html')