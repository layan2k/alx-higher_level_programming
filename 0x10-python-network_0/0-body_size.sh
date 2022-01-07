#!/bin/bash
#Script that displays size of body
curl -sI "$1" | grep 'Content Length'|  cut -f2 -d' '
