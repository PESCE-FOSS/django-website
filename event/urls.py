from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name ='home'),
    path('event/',views.event,name='event'),
    path('contact_us/',views.contact_us,name='contact_us'),
    path('vision/', views.vision, name='vision'),
    
]