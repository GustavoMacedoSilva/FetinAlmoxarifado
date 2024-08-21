#ping_redis.py

import redis
r = redis.Redis(host='localhost', port=6379, db=0)
setter = r.set('foo', 'bar')
getter = r.get('foo')

print(setter, getter)