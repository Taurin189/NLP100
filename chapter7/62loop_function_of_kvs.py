# coding: utf-8
import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)

key_list = r.keys()
japan_artist_list = []
for key in key_list:
    val = r.get(key)
    if val == b'Japan':
        japan_artist_list.append(key)

for artist in japan_artist_list:
    print(artist)
