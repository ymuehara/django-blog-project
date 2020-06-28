from django.urls import path
from . import views  # o ponto . quer dizer diretorio atual

urlpatterns = [
    # '' empty path quer dizer homepage
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
