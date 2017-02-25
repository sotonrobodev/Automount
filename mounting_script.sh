#!/bin/bash
mkdir -p /media/$1
fsck -p /dev/$1
mount -o noatime,sync /dev/$1 /media/$1
