from omxplayer.player import OMXPlayer
audio_path = "audio_files"


def say_play(channel=None):
    player = OMXPlayer(audio_path + "/Play.mp3")
    player.play()


def say_pause(channel=None):
    player = OMXPlayer(audio_path + "/Pause.mp3")
    player.play()


def say_skip(channel=None):
    player = OMXPlayer(audio_path + "/Skip.mp3")
    player.play()


def say_help(channel=None):
    player = OMXPlayer(audio_path + "/Help.mp3")
    player.play()


def say_hungry(channel=None):
    player = OMXPlayer(audio_path + "/Hungry.mp3")
    player.play()


def say_thirsty(channel=None):
    player = OMXPlayer(audio_path + "/Thirsty.mp3")
    player.play()


if __name__ == '__main__':
    say_play()
