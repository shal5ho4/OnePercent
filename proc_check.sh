#プロセス監視
#!/bin/bash

proc_name="/usr/libexec/mysqld"

count=$(ps ax -o command | grep "$proc_name" | grep -v "^grep" | wc -l)

if [ "$count" -eq 0]; then
    echo "[ERROR] process $proc_name is down" >&2
    /home/user/bin/alert.sh
fi
