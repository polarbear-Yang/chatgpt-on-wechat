#!/bin/bash

# Check if restart already in progress
# if [ -f /tmp/restart.lock ]; then
#   echo "Restart already in progress"
#   exit 0
# fi

# Create lock file
# touch /tmp/restart.lock 

cd /home/kaiqian/chatgpt-on-wechat/scripts

./shutdown.sh
echo "shutdown"
./start.sh
echo "start"

# # Remove lock file
# rm /tmp/restart.lock

# Schedule next restart  
echo ./restart.sh | at now + 2 days