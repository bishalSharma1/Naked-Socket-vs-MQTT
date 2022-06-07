#!/bin/bash
c=1
logger () {
    echo "1223" | sudo -S python try2.py &
    echo "logger running"
}

server () {
    python subscribe_file.py &
    echo "server ran..."
}

client () {
    echo "client starting..."
    python sensor_file.py
}

while [ $c -le 1 ] ; # Stop when file.txt has no more lines
do
    echo "experiment no. $c "
    logger
    server
    client
    c=$(( $c + 1 ))
done