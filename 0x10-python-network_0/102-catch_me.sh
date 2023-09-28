#!/bin/bash
#  makes a request to 0.0.0.0:5000/catch_me
curl -sL -X PUT 0.0.0.0:5000/catch_me -H "Origin: You got me!" -o /dev/null -w "You got me!"
