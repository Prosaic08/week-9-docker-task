#!/bin/bash

# #########################################################
# The "test" command will be different depending upon the approach
# you take.
#
# Add whatever commands test your container configuration here.
#
# This file is called by `make test`.
#

MESSAGE="Nobody expects the Spanish Inquisition!"

# Run the Python script inside the send container
docker exec send python send.py "$MESSAGE" > /dev/null

# Wait briefly to ensure listen container processes it
sleep 1

# Check if the listen container logs contain the message
if docker logs task-2-listen-1 2>&1 | grep -qF "$MESSAGE"; then
  echo "$MESSAGE"
  exit 0
else
  exit 1
fi

