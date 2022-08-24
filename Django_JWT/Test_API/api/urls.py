from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacto/', views.contacto, name='contacto'),
    path('galeria/', views.galeria, name='galeria'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('login', views.LoginView.as_view(), name='login'),
    path('user', views.UserView.as_view(), name='user'),
    path('logout', views.LogoutView.as_view(), name='logout'),
]
