#!/bin/bash

for i in {1..100}
do
        now=$(date +%c)
        if [ $i -le 50 ]
        then
			echo "$i<=50"
			rate=`expr $i \* 15 + 500`
        else
			echo "$i>50"
			rate=`expr 2000 - $i \* 15`
        fi
        httperf --server 192.168.3.75 --port 80 --num-conns 80000 --rate=${rate}
        #echo "${date +%s}, ">>log.csv
        echo "$now, $rate" >>log.csv
done


