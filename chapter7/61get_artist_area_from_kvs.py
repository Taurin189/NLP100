# coding: utf-8
import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)
artist_name = input()
print(r.get(artist_name))
