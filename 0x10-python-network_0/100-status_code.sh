#!/bin/bash
# Bash script that sends a requestto URL and display response status code
curl  -s -o /dev/null -w "%{http_code}" "$1"
