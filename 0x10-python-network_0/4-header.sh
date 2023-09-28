#!/bin/bash
#  takes in a URL as an argument, sends a GET request
curl "$1" -sX GET -H "X-School-User-Id:98"
