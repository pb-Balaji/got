from django.shortcuts import render
from user.models import Enquiry

# Create your views here.

def home(request):
    return render(request,'home/home.html',context={'title':"home page"})

def enquiry_detail(request):
    enquirydata =Enquiry.objects.all()
    context={'title':"Enquiry page", 'enquirydata':enquirydata}
    return render(request,'home/enquiry.html',context)