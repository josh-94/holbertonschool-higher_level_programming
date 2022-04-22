#!/bin/bash
# Script takes URL, sends a request and displays the size of the body of th response.
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f 2