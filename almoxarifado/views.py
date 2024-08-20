from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

class HomeView(TemplateView):
    template_name = 'home.html'

def contato_page(request):
    return render(request, "contato.html")

def sendEmail(request):
    send_mail(
        'Fala Dog', # titulo do email
        'E O PIX GALERINHA? NADA AINDA? FAZ O PIX!!! Apenas testes ok? by nosso grupo from FETIN.', # mensagem que sera enviada
        'settings.EMAIL_HOST_USER', # importa algumas configurações do projeto 
        ['macedo.gustavo@ges.inatel.br', 'henrique.issao@gec.inatel.br', 'guilhermebrito@gec.inatel.br'], # lista de emails que o django vai enviar esta mensagem
        fail_silently=False
    )
    return HttpResponse('Enviado')