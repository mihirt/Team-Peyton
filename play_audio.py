from omxplayer.player import OMXPlayer
audio_path = "audio_files"

def say_play():
    player = OMXPlayer(audio_path+"/Play.mp3")
    player.play()

def say_pause():
    player = OMXPlayer(audio_path+"/Pause.mp3")
    player.play()

def say_skip():
    player = OMXPlayer(audio_path+"/Skip.mp3")
    player.play()

def say_help():
    player = OMXPlayer(audio_path+"/Help.mp3")
    player.play()

def say_hungry():
    player = OMXPlayer(audio_path+"/Hungry.mp3")
    player.play()

def say_thirsty():
    player = OMXPlayer(audio_path+"/Thirsty.mp3")
    player.play()


say_play()
say_pause()
say_skip()
say_help()
say_hungry()
say_thirsty()
print("done")
