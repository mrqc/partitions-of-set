#!/bin/bash
rm partitionsprecalculations.py
for i in $(seq 1 11); do time python partitions.counting.iterative.py $i >> partitionsprecalculations.py; echo "partition $i done"; done
