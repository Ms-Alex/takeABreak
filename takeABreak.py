# -*- coding: utf-8 -*-
"""
A program that will remind you to take a break;
 via opening the browser and playing a YT video.
 
"""

import time
import webbrowser

totalBreaks = 3
breakCount = 0

print("This program started at " + time.ctime()) # ctime() is current time

while (breakCount < totalBreaks):
    time.sleep(10) #in seconds
    webbrowser.open("https://www.youtube.com/watch?v=ObnSM-6DNpM")
    breakCount += 1