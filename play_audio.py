from playsound import playsound
import os
audio_path = "audio_files"

def say_play():
    playsound(audio_path+"/Play.mp3")

def say_pause():
    playsound(audio_path+"/Pause.mp3")

def say_skip():
    playsound(audio_path+"/Skip.mp3")

def say_help():
    playsound(audio_path+"/Help.mp3")

def say_hungry():
    playsound(audio_path+"/Hungry.mp3")

def say_thirsty():
    playsound(audio_path+"/Thirsty.mp3")


say_play()
say_pause()
say_skip()
say_help()
say_hungry()
say_thirsty()
print("done")
