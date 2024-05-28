from django.urls import include, path
from .views import loginPage, logoutUser

urlpatterns = [
    ##path('endereço/', MinhaView.as_view(), name = 'nome-da-url'), colinha
    path('', include('inventario.urls')),
]