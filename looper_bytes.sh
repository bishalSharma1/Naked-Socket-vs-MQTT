#!/bin/bash
c=1
logger () {
    echo "1223" | sudo -S python try2.py &
    echo "logger running"
}

server () {
    python subscribe_bytes.py &
}

client () {
    python sensor_bytes.py
}

while [ $c -le 100 ] ;
do
    echo "experiment no. $c "
    logger
    server
    client
    c=$(( $c + 1 ))
done
