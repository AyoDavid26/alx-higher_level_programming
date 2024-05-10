#!/bin/bash
# a bash script that takes a URL and sends a request to that URL
curl -s "$1" | wc -c
