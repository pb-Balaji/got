from django.urls import path
from home import views



urlpatterns = [
    path('home/',views.home,name='home'),
    path('enquiry_detail/',views.enquiry_detail,name='enquiry_detail'),

]