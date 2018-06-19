#!/bin/bash
for i in {1..5}
do
	httperf --server 192.168.3.75 --port 80 --num-conns 50000 --rate 2000
done
