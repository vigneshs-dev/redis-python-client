import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

print(f"Name: {r.get('Name')}") 
