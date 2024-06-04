#!/bin/bash
# Bash script that takesin a URL and displays all HTTP methods
curl -sI "$1"| grep "Allow"| cut -d " " -f 2-
