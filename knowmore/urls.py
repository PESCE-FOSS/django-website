from django.urls import path
from . import views

urlpatterns = [
    path('ourteams',views.ourteams,name ='ourteams'),
    path('ourwork',views.ourwork,name ='ourwork'),
   
]