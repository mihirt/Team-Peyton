import pygame
audio_path = "audio_files"
pygame.init()
pygame.mixer.init()

def say_play(channel=None):
    file = audio_path + "/Play.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(3)


def say_pause(channel=None):
    file = audio_path + "/Pause.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(3)


def say_skip(channel=None):
    file = audio_path + "/Skip.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(3)


def say_help(channel=None):
    file = audio_path + "/Help.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(3)


def say_hungry(channel=None):
    file = audio_path + "/Hungry.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(3)


def say_thirsty(channel=None):
    file = audio_path + "/Thirsty.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(3)


if __name__ == '__main__':
    say_play()
