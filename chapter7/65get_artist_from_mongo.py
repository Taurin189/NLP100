# coding: utf-8
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
artist_col = client.artist['artist']
artist_datas = artist_col.find({"name": "Queen"})
for data in artist_datas:
    print(data)