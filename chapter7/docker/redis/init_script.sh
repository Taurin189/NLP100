#!/bin/bash
count=0
redis-server &
cat artist.txt | while read line
do
  echo $line | redis-cli --pipe
  count=$(expr $count + 1)
  if [ $count -ge 9 ] ; then
    sleep 1
    count=0
  fi
done
while true; do sleep 10; done