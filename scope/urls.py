from . import views
from django.urls import path,include

urlpatterns = [
    
   
   
    
    path('', views.HomePage,name="home"),
    path('signup',views.SignupPage,name='signup'),
    path('login',views.LoginPage,name='loginpage'),
    path('about', views.about,name="about"),
    path('contact', views.contact,name="contact"),
    path('logout',views.LogoutPage,name='logout'),
    path('loginpage',views.LoginPage,name='loginpage'),
    path('registration',views.registration,name='registration'),
]