# users/urls.py
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, SignInView
from django.urls import path

app_name = "users"


urlpatterns = [
   path("signup/", RegisterView.as_view(), name='register'),
   path("signin/", SignInView.as_view(template_name='users/signin.html'), name='login'),
   path("logout/", LogoutView.as_view(template_name='users/logout.html'), name='logout'),

]
