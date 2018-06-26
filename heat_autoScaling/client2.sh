#!/bin/bash

for i in {1..10}
do
        rate=`expr $i \* 100 + 1000`
        httperf --server 192.168.3.75 --port 80 --num-conns 50000 --rate=${rate}
        date +%s
done

