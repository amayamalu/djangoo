"""calculator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from operations import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/',views.AdditionView.as_view(),name="add"),
    path('sub/',views.SubtractionView.as_view(),name="sub"),
    path('mul/',views.MultiplicationView.as_view(),name="multi"),
    path('div/',views.DivisionView.as_view(),name="div"),
    path('fact/',views.FactorialView.as_view(),name="fact"),
    path('prime/',views.PrimeView.as_view(),name="prime"),
    path('armstrong/',views.ArmstrongView.as_view(),name="armstrong"),
    path('palindrome/',views.PalindromeView.as_view(),name="palindrome"),
    path('even/',views.EvenView.as_view(),name="even"),
    
    path('health/',views.HealthView.as_view(),name="health"),
    
    path('temp/',views.TemperatureView.as_view(),name="temp"),
   
    path('exponent/',views.ExponentView.as_view(),name="expoenent"),
    path('login/',views.LoginView.as_view(),name="login"),  
    path('register/',views.RegistrationView.as_view(),name="register"),
    
    path("geo/",views.GeoView.as_view()),
    path('geoo/',views.GeooView.as_view()),
    path('',views.HomeView.as_view(),name="home"),
    
]
    
    
    
    
    
    
   

 

