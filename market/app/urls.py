from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', views.ProductoViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('contacto/', views.contacto, name='contacto'),
    path('galeria/', views.galeria, name='galeria'),
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path('listar-productos/', views.listar_productos, name='listar_productos'),
    path('modificar-producto/<id>/', views.modificar_producto, name='modificar_producto' ),
    path('eliminar-producto/<id>/', views.eliminar_producto, name='eliminar_producto'),
    path('registro/', views.registro, name='registro'),
    path('api/', include(router.urls)),
    path('register', views.RegisterView.as_view(), name='register'),
    path('loginview', views.LoginView.as_view(), name='loginview'),
    path('user', views.UserView.as_view(), name='user'),
    path('logoutview', views.LogoutView.as_view(), name='logoutview'),
]