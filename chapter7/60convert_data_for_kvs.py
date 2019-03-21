# coding: utf-8
import json

artist_dict = {}
with open("docker/artist.json", "r") as f:
    for line in f.readlines():
        tmp_artist_dict = {}
        data = json.loads(line)
        if 'area' in data.keys():
            artist_dict.update({data['name']: data['area']})

with open("docker/redis/artist.txt", "w") as f:
    for k, v in artist_dict.items():
        k = k.replace("'", "\\'")
        v = v.replace("'", "\\'")
        k = k.replace("\"", "\\")
        v = v.replace("\"", "\\")
        f.write("SET \"" + k + "\" \"" + v + "\"\n")

print(artist_dict)