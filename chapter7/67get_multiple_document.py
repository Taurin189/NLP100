# coding: utf-8
from pymongo import MongoClient

name = input()
output_list = []

client = MongoClient('localhost', 27017)
artist_col = client.artist['artist']
artist_datas = artist_col.find({'aliases': {'$exists': True}})
for artist_data in artist_datas:
    for alias in artist_data['aliases']:
        if alias['name'] == name:
            print(artist_data)