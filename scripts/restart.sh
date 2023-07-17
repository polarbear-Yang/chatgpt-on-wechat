#!/bin/bash

# Restart the app
./shutdown.sh
./start.sh

# Schedule the next restart in 3 days
echo ./restart.sh | at now + 3 days