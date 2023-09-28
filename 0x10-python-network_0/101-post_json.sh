#!/bin/bash
#  sends a JSON POST request to a URL passed as 1st arg
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
