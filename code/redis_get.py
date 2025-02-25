import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

print(f"User Name: {r.get('Name')}") 
