#!/bin/bash
# 
# require:  mpc
# apt-get install mpc

source ~/.bashrc

# saver to add in .bashrc ;)
# MOBILE_IP=""
# SERVER_NAME="password@ip" 
SERVER_PORT="6600"

echo "Mobile: "
echo $MOBILE_IP
echo "Server:"
echo $SERVER_NAME

function get_state() {
    COUNT=$(ping "$MOBILE_IP" -c 3 | grep "ttl=" | wc -l)

    if [ "$COUNT" == "0" ]; then
        echo 0
    else
        echo 1
    fi
}


LASTSTATE="-1"
#while true
#do
while true;
do
    # get the actual state
    STATE=$(get_state)

    if [ "$LASTSTATE" == "$STATE" ]; then
        # if found state wasn't changed, wait 3 seconds.
        sleep 3
    else
        # if found state was changed
        if [ "$STATE" == "0" ]; then
           # it the state result was not found, pause the music
           SEND_COMMAND="pause"
        else
           # else means the state result was found, play the music
           SEND_COMMAND="toggle" #play
        fi

        #send command to the server
        mpc -h "$SERVER_NAME" -p "$SERVER_PORT" "$SEND_COMMAND"

        # save last state
        LASTSTATE=$STATE
    fi
done
