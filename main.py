from redis import Redis

r = Redis(host='localhost', port='6379', decode_responses=True)

r.set('foo', 'bar')

print(r.get('foo'))