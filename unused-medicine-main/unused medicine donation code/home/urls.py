from django.contrib import admin
from django.urls import path, include
from . import views
from .models import ngodetail, donordetail, medicine, doctordetail
from .forms import CreateUserForm, CreatengoForm, CreateDoctorForm
from .forms import CreateUserForm, CreatengoForm, CreateDoctorForm
urlpatterns = [
    path('', views.index, name='home'),
    path('registerdonor/', views.registerdonor, name="registerdonor"),
    path('registerseller/', views.registerseller, name="registerseller"),
    path('registerngo/', views.registerngo, name="registerngo"),
    path('login/', views.loginpage, name="login"),  
    path('logout/', views.logoutuser, name="logout"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('contact/', views.contact, name="contact"),
    path('NGO-Details/', views.detailsngo, name="detailsngo"),
    path('Donor-Details/', views.detailsdonor, name="detailsdonor"),
    path('adminaction/', views.adminaction, name="adminaction"),
    path('admindashboard/', views.admindashboard, name="admindashboard"),
    path('NGOdashboard/', views.ngodashboard, name="ngodashboard"),
    path('donordashboard/', views.donordashboard, name="donordashboard"),
    path('donorprofile/', views.donorprofile, name="donorprofile"),
    path('ngoprofile/', views.ngoprofile, name="ngoprofile"),
    path('medicinedonation/', views.medicinedonation, name="medicinedonation"),
    path('registerdoctor/', views.Registerdoctor, name='registerdoctor'),
    # path('thankyou/', views.thankyou, name='thankyou'),
    path('search_ngos/', views.search_ngos,name='search_ngos'),
    path('', views.navbar,name='navbar'),
    path('user_login/', views.user_login,name='user_login'),
    path('about/', views.about,name='about'),
    path('user_registration/', views.user_registration,name='user_registration'),
    path('user_home/', views.user_home,name='user_home'),
    path('contact/', views.contact,name='contact'),
    path('admin_login/', views.admin_login,name='admin_login'),
    path('admin_registration/', views.admin_registration,name='admin_registration'),
    path('admin_home/', views.admin_home,name='admin_home'),
    path('doctor_registration/', views.doctor_registration,name='doctor_registration'),
    path('doctor_login/', views.doctor_login,name='doctor_login'),
    path('ngo_login/', views.ngo_login,name='ngo_login'),
    path('user_logout/', views.user_logout,name='user_logout'),
    path('admin_logout/', views.admin_logout,name='admin_logout'),
    path('doctor_logout/', views.doctor_logout,name='doctor_logout'),
    path('doctor_home/', views.doctor_home,name='doctor_home'),
    path('ngo_registration/', views.ngo_registration,name='ngo_registration'),
    path('upload_medicine/', views.upload_medicine,name='upload_medicine'),
    # Use views.Registerdoctor instead of Registerdoctor
    # path('registerdoctor/', RegisterDoctorView.as_view(), name='registerdoctor'),
    #  path('', HomePageView.as_view(), name='home'),
    
    
]
