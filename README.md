# FetinAlmoxarifado

Para instalar todos os plugins necessarios automaticamente basta executar "pip install -r requirements.txt" na mesma pasta do projeto
lembrar de sempre que adicionar um novo plugin de python ao projeto atualizar o arquivo requirements.txt usando "pip freeze > requirementes.txt"

# Usuario Administrador

O painel de administrador esta configurado na url /admin e o login e senha criados são ambos "admin", pedindo email é admin@gmail.com


# Execução com as tasks programadas

IMPORTANTE ESTAR COM TODAS AS LIBS DE PYTHON USADAS NO PROJETO ATUALIZADAS

1. Instalar o Memurai for redis dev version usando o comando (winget install "Memurai Developer") no windows powershell aberto como administrador
2. Reinicie o computador para iniciar o servidor do memurai
3. Execute o arquivo "ping_memurai.py" e ele deve ter com saida "True b'bar'" caso contrario ouve algum erro
4. Executar o servidor do django normalmente com "py manage.py runserver"
5. Executar em outro prompt o comando "celery -A almoxarifado worker --loglevel=INFO --without-gossip --without-mingle      --without-heartbeat -Ofair --pool=solo"
6. Executar em mais um prompt o comando "celery -A almoxarifado beat -l info"
7. A partir de agora para poder encerrar o servidor do django precisa primeiro abrir outro prompt e executar o comando "celery -A almoxarifado control shutdown" depois que ele apresentar erro pode fechar os prompts e fechar o servidor do django normalmente

o arquivo flush_redis.py pode ser executado para limpar as filas de tarefas do celery em caso de problemas na sua execução
