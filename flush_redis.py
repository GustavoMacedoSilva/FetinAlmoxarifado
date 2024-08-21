import redis

# Conecte-se ao Redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)

# Liste as filas do Celery
queues = r.keys('celery*')

# Apague cada fila
for queue in queues:
    r.delete(queue)
    print(f"Fila {queue} limpa.")