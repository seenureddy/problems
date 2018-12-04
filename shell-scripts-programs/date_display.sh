#!/bin/sh

for i in 1 2 3 4 5 6 7 8; do date >> log.txt ; echo $i >> log.txt ; sleep 1; done
