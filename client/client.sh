#!/bin/bash

for i in {1..100}
do
        now=$(date +%c)
        if [ $i -le 20 ]
        then
			echo "$i<=20"
			rate=`expr $i \* 10 + 300`
		elif [ $i -le 30 ]
		then
			echo "$i<=30"
			rate=`expr $i \* 50 + 300`
		elif [ $i -le 50 ]
		then
			echo "$i<=50"
			rate=`expr $i \* 10 + 300`
        else
			echo "$i>50"
			rate=`expr 1300 - $i \* 10`
        fi
        httperf --server 192.168.3.75 --port 80 --num-conns 60000 --rate=${rate}
        #echo "${date +%s}, ">>log.csv
        echo "$now, $rate" >>log.csv
done


