#!/usr/bin/env sh
echo "waiting for 60 seconds to record uptime"
sleep 10
echo "record current uptime to /var/log/uptime.log"
cp /proc/uptime /var/log/uptime.log
sleep 50
