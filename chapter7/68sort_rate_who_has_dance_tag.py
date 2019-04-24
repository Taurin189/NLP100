# coding: utf-8
from pymongo import MongoClient

dance_tag_dict = {}

client = MongoClient('localhost', 27017)
artist_col = client.artist['artist']
artist_datas = artist_col.find({'tags': {'$exists': True}})
for artist_data in artist_datas:
    for alias in artist_data['tags']:
        if alias['value'] == 'dance':
            if 'rating' in artist_data.keys():
                dance_tag_dict.update({artist_data['name']: artist_data['rating']['count']})
for k, v in sorted(dance_tag_dict.items(), key=lambda x: -x[1])[:10]:
    print(str(k) + ": " + str(v))