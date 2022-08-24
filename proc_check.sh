#!/bin/bash
  
proc1="/usr/sbin/rabbitmq-server"
proc2="/home/onepercentadmin/django_projects/OnePercent/env/bin/celery"
proc3="/usr/sbin/nginx"

count1=$(ps ax -o command | grep "$proc1" | grep -v "^grep" | wc -l)
count2=$(ps ax -o command | grep "$proc2" | grep -v "^grep" | wc -l)
count3=$(ps ax -o command | grep "$proc3" | grep -v "^grep" | wc -l)

for ((i=1; i<=3; i++)); do
    proc="proc${i}"
    count="count${i}"

    if [ ${!count} -eq 0 ]; then
        echo "[ERROR] process $proc is down" >&2
        /home/onepercentadmin/alert.sh "[ERROR] process $proc has been down"
    fi
done
