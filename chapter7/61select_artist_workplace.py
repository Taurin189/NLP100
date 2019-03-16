# coding: utf-8
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
artist_col = client.artist['artist']
artist_datas = artist_col.find()
for data in artist_datas:
    tmp_test = data['name'] + " : "
    if 'area' in data.keys():
        tmp_test += data['area']
    print(tmp_test)
