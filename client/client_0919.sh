#!/bin/bash

for i in {1..120}
do
        now=$(date +%c)
        if [ $i -le 20 ]
        then
			echo "$i<=20"
			rate=`expr $i \* 10 + 800`
		elif [ $i -le 30 ]
		then
			echo "$i<=40"
			rate=`expr $i \* 50 + 1000`
		elif [ $i -le 50 ]
		then
			echo "$i<=60"
			rate=`expr $i \* 10 + 800`
        else
			echo "$i>60"
			rate=`expr 2600 - $i \* 20`
        fi
        httperf --server 192.168.3.75 --port 80 --num-conns 80000 --rate=${rate}
        #echo "${date +%s}, ">>log.csv
        echo "$now, $rate" >>log.csv
done


