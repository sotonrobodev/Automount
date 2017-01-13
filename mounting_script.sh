#!/bin/bash

pmount /dev/$1
python3 /media/$1/main.py
pumount /dev/$1
