#!/bin/bash
echo "Scraper initialised"
while true; do
   python -m app
   echo "Scraper ended"
   sleep $[60 * 60 * 12]
done