#!/bin/bash
# sends request to given URL and displays the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
