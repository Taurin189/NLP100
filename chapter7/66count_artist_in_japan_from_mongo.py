# coding: utf-8
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
artist_col = client.artist['artist']
artist_datas = artist_col.find({"area": "Japan"})
print(artist_datas.count())
