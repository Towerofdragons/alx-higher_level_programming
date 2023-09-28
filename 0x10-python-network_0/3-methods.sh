#!/bin/bash
# Take URL display all allowed methods
curl -Is 0.0.0.0:5000/route_4 | grep "Allow" | cut -d " " -f2-
