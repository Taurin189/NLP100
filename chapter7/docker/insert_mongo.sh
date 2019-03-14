#!/bin/bash
cat ./artist.json | while read line
do
  mongo --eval "printjson(db.artist.insert($line))"
done
