from django.urls import path
from django.contrib.auth import views as auth_views
from bases import views as vistas
from bases.views import  HomeSinPrivilegios


urlpatterns = [
    path('', vistas.home, name='home'),
    path('login/',auth_views.LoginView.as_view(template_name='bases/login-2.html'),
                name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='bases/login-2.html'),
                name='logout'),
    path('sin_privilegios/', HomeSinPrivilegios.as_view(), name='sin_privilegios'),

]
