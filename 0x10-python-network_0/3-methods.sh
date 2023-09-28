#!/bin/bash
# Take URL display all allowed methods
curl -Is "$1" | grep "Allow" | cut -d " " -f2-
