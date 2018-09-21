#!/bin/bash

> lograte.csv
for i in {1..120}
do
	now=$(date +%c)
	echo $a "show stat" | sudo nc -U /var/run/haproxy/haproxy.sock | cut -d "," -f 34 | tr "\n" "\t" >> lograte.csv
	echo "$now" >>lograte.csv

done
