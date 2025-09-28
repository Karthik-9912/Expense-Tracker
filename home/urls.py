from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home1'),
    path('register/',views.register,name='register'),
    path('login/',views.log_in,name='login'),
]
