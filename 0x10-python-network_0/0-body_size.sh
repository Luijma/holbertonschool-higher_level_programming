#!/bin/bash
# Uses URL and makes http request then displays size of response
curl -s $URL | wc -c
