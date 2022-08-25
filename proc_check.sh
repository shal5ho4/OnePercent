#!/bin/bash
  
proc1="/usr/sbin/rabbitmq-server"
proc2="/usr/sbin/nginx"
proc3=""
proc4=""


for ((i=1; i<=4; i++)); do
    proc="proc${i}"
    count=$(ps ax -o command | grep "${!proc}" | grep -v "^grep" | wc -l)

    if [ $count -eq 0 ]; then
        echo "[ERROR] process ${!proc} is down" >&2
        /home/onepercentadmin/alert.sh "[ERROR] process ${!proc} has been down"
    fi
done
