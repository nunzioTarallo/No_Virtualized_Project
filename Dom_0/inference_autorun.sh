#!/bin/bash


python3 connection.py

start=$(date +%s.%N)

python3 voter.py

duration=$(echo "$(date +%s.%N) - $start " | bc)
LC_NUMERIC="en_US.UTF-8" execution_time= printf "%.2f\n" $duration >>tempi.txt

