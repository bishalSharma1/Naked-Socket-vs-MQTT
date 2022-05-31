#!/bin/bash
c=1
logger () {
    echo "1223" | sudo -S python try2.py &
    echo "logger running"
}

server () {
    python subscribe_bytes.py &
    echo "server ran..."
}

client () {
    python sensor_bytes.py
    echo "client ran..."
}

while [ $c -le 500 ] ; # Stop when file.txt has no more lines
do
    echo "experiment no. $c "
    logger
    server
    client
    c=$(( $c + 1 ))
done
