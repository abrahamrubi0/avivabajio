from django.urls import path
from django.contrib.auth import views as auth_views
from app import views as vistas


urlpatterns = [
    path('conferencias/', vistas.conferencias, name = 'conferencias'),
    path('conferencia/', vistas.conferencia_view, name = "conferencia_view"),
    path('blogs/', vistas.blog_list, name = "blog_list"),
    path('blog/', vistas.blog_view, name = "blog"),
    path('contacto/', vistas.contacto, name = "contacto"),

 ]
