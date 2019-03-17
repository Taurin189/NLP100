#!/bin/bash
# cat ./artist.json | while read line
# do
#  echo $line > /dev/stdout
  # mongo --eval "printjson(db.artist.insert($line))"
# done
mongoimport --db artist --collection artist --file artist.json