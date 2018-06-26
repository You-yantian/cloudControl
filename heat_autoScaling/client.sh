#!/bin/bash
for i in {1..10}
do
	httperf --server 192.168.3.75 --port 80 --num-conns 500000 --rate 1500
done
