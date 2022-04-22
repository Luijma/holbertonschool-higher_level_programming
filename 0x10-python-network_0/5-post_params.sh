#/bin/bash
# Sends post request to given URL with email parameter
curl -sX POST -d "email=test@gmail.com&subject=I will always be here ofr PLD" "$1"
