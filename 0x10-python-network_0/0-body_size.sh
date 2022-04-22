#!/bin/bash
# Uses URL and makes http request then displays size of response
curl -s "$1" | wc -c
