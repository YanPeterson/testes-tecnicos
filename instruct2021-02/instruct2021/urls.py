from django.urls import path
from app_projetos import views

urlpatterns = [
    #rota, view responsável, nome de ref
    path('', views.home, name='home'),
    #sla.com/ssla
    #path('ssla')
]
