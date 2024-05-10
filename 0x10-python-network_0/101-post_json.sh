#!/bin/bash
# Bash script that sends a JSON POST req and display respponse body
curl -sL -H "content-type:application/json"  -d @"$2" -X POST "$1"
