# Make a program to said by computer for the name which sotred in list 

import win32com.client as win
speaker = win.Dispatch("SAPI.spVoice")

list = ["Jaimn", "Dhruvil", "Darshan"]

for i in list :
    shoutout = speaker.speak(f"Shoutout to {list[i]}")