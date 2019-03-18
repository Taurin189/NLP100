#!/bin/bash
redis-server &
sleep 20; (cat artist.txt; sleep 10) | redis-cli --pipe
while true; do sleep 10; done