#This is a program to build a video_alarm for reminding of breaks while working. It automatically opens webbrowser for specific address.
# We import two of these modules to use them for enhancement of programs.
import time
import webbrowser

total_breaks = 4
break_count = 0

print("This program started at" time.ctime())
while(break_count < total_breaks):
    time.sleep(10) # This is in seconds.
    webbrowser.open("https://www.youtube.com/watch?v=ocwnns57cYQ")
    break_count += 1
