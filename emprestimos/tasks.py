from celery import shared_task
from emprestimos.models import Emprestimo
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail

@shared_task
def expirationChecker():
    data_atual = timezone.now().date() # encontra a data do dia
    vencidos = Emprestimo.objects.filter(data_de_devolucao__lt=data_atual) # recebe uma lista com todos os emails de alunos que tem emprestimos vencidos
    vencimento_hoje = Emprestimo.objects.filter(data_de_devolucao=data_atual) # recebe uma lista com todos os emails de alunos que tem emprestimos que irão vencer no dia 
    vencimento_em_breve = Emprestimo.objects.filter(data_de_devolucao=(data_atual + timedelta(days = 2))) # recebe uma lista com todos os emails de alunos que tem emprestimos que irão vencer no daqui 2 dias
    for emprestimo in vencidos:
        send_mail(
            'Emprestimo Vencido', # titulo do email
            f'Boa tarde {emprestimo.aluno.user.username} voce tem um emprestimo de numero {emprestimo.id} vencido na data de {emprestimo.data_de_devolucao} registrado em seu nome aqui no almoxarifado do inatel, por favor entre em contato ou venha pessoalmente no almoxarifado do inatel para regularizar seu emprestimo.', # mensagem que sera enviada
            'settings.EMAIL_HOST_USER', # importa algumas configurações do projeto 
            [f'{emprestimo.aluno.user.email}'], # lista de emails que o django vai enviar esta mensagem
            fail_silently=False
        )
    for emprestimo in vencimento_hoje:
        send_mail(
            'Lembrete de Emprestimo', # titulo do email
            f'Boa tarde {emprestimo.aluno.user.username} voce tem um emprestimo de numero {emprestimo.id} que esta vencendo hoje {data_atual} não se esquça de devolvelos a tempo no almoxarifado ou entrar em contado para estender seu praso caso precise de mais tempo.', # mensagem que sera enviada
            'settings.EMAIL_HOST_USER', # importa algumas configurações do projeto 
            [f'{emprestimo.aluno.user.email}'], # lista de emails que o django vai enviar esta mensagem
            fail_silently=False
        )
    for emprestimo in vencimento_em_breve:
        send_mail(
            'Lembrete de Emprestimo', # titulo do email
            f'Boa tarde {emprestimo.aluno.user.username} apenas passando para lembrar que seu emprestimo numero {emprestimo.id} esta prestes a vencer em {emprestimo.data_de_devolucao} não se esqueça de devolver os items do emprestimo no almoxarifado ate os dia do vencimento ou então entrar em contato conosco para que possamos estender seu praso caso precise ficar com os items por mais tempo', # mensagem que sera enviada
            'settings.EMAIL_HOST_USER', # importa algumas configurações do projeto 
            [f'{emprestimo.aluno.user.email}'], # lista de emails que o django vai enviar esta mensagem
            fail_silently=False
        )
    