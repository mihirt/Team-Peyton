import pygame
audio_path = "audio_files"
pygame.init()
pygame.mixer.init()

def B1(channel=None):
    file = audio_path + "/Play.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(3)


def B2(channel=None):
    file = audio_path + "/Pause.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(3)


def B3(channel=None):
    file = audio_path + "/Skip.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(3)


def B4(channel=None):
    file = audio_path + "/Help.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(3)


def B5(channel=None):
    file = audio_path + "/Hungry.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(3)


def B6(channel=None):
    file = audio_path + "/Thirsty.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(3)


if __name__ == '__main__':
    say_play()
