from django.urls import path
from .views import HomeView, EquipsView

urlpatterns = [
    ##path('endereço/', MinhaView.as_view(), name = 'nome-da-url'), colinha
    path('', HomeView.as_view(), name = 'home_page'),
    path('equipamentos/', EquipsView.as_view(), name = 'equipamentos'),
]