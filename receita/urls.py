from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('receita/<slug:slug>', views.detalhe_receita, name='detalhe_receita'),
]
