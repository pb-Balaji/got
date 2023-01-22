from django.urls import path
from user import views



urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login_view, name='login'),
    path('register/',views.register_view,name='register'),
    path('logout/',views.logout_view,name='logout'),
    path('services/',views.services,name='services'),
    path('about/',views.about,name='about'),
    path('team/',views.team,name='team'),
    path('contact/',views.contact,name='contact'),
    path('features/',views.features,name='features'),
    path('enquiry/',views.enquiry,name='enquiry'),
]
