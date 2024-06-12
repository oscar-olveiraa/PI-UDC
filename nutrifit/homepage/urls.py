from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    #path('myprofile/', views.principal, name='principal'),
    path('perfil/', views.perfil, name='perfil'),
    path('actualizar/', views.actualizar_perfil, name='actualizar'),
    path('cambiar_contrasenha/', views.cambiar_contrasenha, name='cambiar_contrasenha'),
    path('aux/createuser/', views.createuser, name='createuser')
]