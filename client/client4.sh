#!/bin/bash

for i in {1..20}
do
        now=$(date +%c)
		echo "time is: $i"
		rate=`expr $i \* 100 + 1000`
        httperf --server 192.168.3.75 --port 80 --num-conns 80000 --rate=${rate}
        #echo "${date +%s}, ">>log.csv
        echo "$now, $rate" >>log.csv
done
