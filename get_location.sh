#!/bin/bash
LOCATION_RESPONSE=$(curl -s http://ipinfo.io/json)

LOCATION=$(echo $LOCATION_RESPONSE| jq -r '.loc')

curl -X POST http://127.0.0.1:5000/my_gps \
    -H "Content-Type: application/json" \
    -d "{\"location\":\"$LOCATION\"}"
