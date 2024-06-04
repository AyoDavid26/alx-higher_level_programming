#!/bin/bash
# Bash script that takes in a URL, send a GEt request and display 
curl -sfL "$1" -X GET
