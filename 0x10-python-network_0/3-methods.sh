#!/bin/bash
# takes url and displays all http methods server accepts
curl -sI "$1" | grep "Allow: " | sed -n -e 's/^Allow: //p'
