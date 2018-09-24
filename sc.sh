#!/bin/bash
cd /home/soandso/Documents/HACKUTD/Screenshots
adb shell screencap -p /sdcard/screen.png
adb pull /sdcard/screen.png
adb shell rm /sdcard/screen.png

