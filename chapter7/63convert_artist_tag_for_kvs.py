# coding: utf-8
import json

artist_dict = {}
with open("docker/artist.json", "r") as f:
    for line in f.readlines():
        tmp_artist_dict = {}
        data = json.loads(line)
        if 'tags' in data.keys():
            artist_dict.update({data['name']: data['tags']})

with open("docker/redis2/artist_tag.txt", "w") as f:
    for k, v in artist_dict.items():
        print(v)
        v_str = str(v)
        k = k.replace("'", "\\'")
        v_str = v_str.replace("'", "\\'")
        k = k.replace("\"", "\\")
        v_str = v_str.replace("\"", "\\")
        f.write("SET \"" + k + "\" \"" + v_str + "\"\n")

print(artist_dict)