#!/bin/bash

for i in {1..10}
do
        now=$(date +%c)
		rate=`expr $i \* 50 + 1000`
        httperf --server 192.168.3.75 --port 80 --num-conns 50000 --rate=${rate}
        echo "$now, $rate" >>log.csv

done

