from django.urls import path
from django.contrib.auth import views as auth_views
from  .views import *
from .forms import *
app_name='core'

urlpatterns = [
    path('',index,name='index'),
    path('contact/',contact,name='contact'),
    path('about/',about,name='about'),
    path('privacy/',privacy,name='privacy'),
    path('terms/',terms,name='terms'),
    path('signup/',signup,name='signup'),
    path('logout/', logoutUser,name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=Loginform),name='login'),
]