import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)
r.set('User Name', 'Vicky')

print("Value set Successfully!")