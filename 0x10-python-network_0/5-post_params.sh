#!/bin/bash
# Bash script that takes in URL, sends POST request and displays response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
