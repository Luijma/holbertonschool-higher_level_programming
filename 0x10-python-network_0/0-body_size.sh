#!/bin/bash
# Uses URL and makes http request then displays size of response
URL=$1
curl -s "$URL" | wc -c
