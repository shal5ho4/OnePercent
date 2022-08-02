#通知処理
#!/bin/bash

LINE_ACCESS_TOKEN=""

function line_notify() {
  MESSAGE=$1
  curl -X POST -H "Authorization: Bearer ${LINE_ACCESS_TOKEN}" -F "message=$MESSAGE" https://notify-api.line.me/api/notify
 }
 
 line_notify "エラーが発生しました。"
