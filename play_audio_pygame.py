import pygame
audio_path = "audio_files"
pygame.init()
pygame.mixer.init()

def B1(channel=None):
    file = audio_path + "/bathroom.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(3)


def B2(channel=None):
    file = audio_path + "/drink.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(3)


def B3(channel=None):
    file = audio_path + "/walk.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(3)


def B4(channel=None):
    file = audio_path + "/help.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(3)


def B5(channel=None):
    file = audio_path + "/hug.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(3)


def B6(channel=None):
    file = audio_path + "/hungry.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(3)

def B7a(channel=None):
    file = audio_path + "/play.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(3)

def B7b(channel=None):
    file = audio_path + "/pause.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(3)

def B8(channel=None):
    file = audio_path + "/skip.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(3)

if __name__ == '__main__':
    say_play()
