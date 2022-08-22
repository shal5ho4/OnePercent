#!/bin/bash
  
proc1="/usr/sbin/rabbitmq-server"
proc2="celery"

count1=$(ps ax -o command | grep "$proc1" | grep -v "^grep" | wc -l)
count2=$(ps ax | grep "$proc2" | wc -l)

if [ "$count1" -eq 0 ]; then
    echo "[ERROR] process $proc1 has been down" >&2
    /home/onepercentadmin/django_projects/OnePercent/alert.sh "[ERROR] process $proc1 has been down"
fi

if [ "$count2" -lt 2 ] ; then
        echo "[ERROR] process $proc2 is down" >&2
        /home/onepercentadmin/django_projects/OnePercent/alert.sh "[ERROR] process $proc2 has been down"
fi
