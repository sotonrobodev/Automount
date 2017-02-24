#!/bin/bash

pmount /dev/$1
cd /media/$1
if [ -f main.py ]; then
  python3 main.py
else
  echo "cannot find main.py on this usb stick" > output.log
fi
cd /
pumount /dev/$1
