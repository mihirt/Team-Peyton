import pygame
audio_path = "audio_files"
pygame.init()
pygame.mixer.init()

def B1(channel=None):
    print("clicked 1")
    file = audio_path + "/bathroom.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(3)


def B2(channel=None):
    print("clicked 2")
    file = audio_path + "/drink.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(3)


def B3(channel=None):
    print("clicked 3")
    file = audio_path + "/walk.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(3)


def B4(channel=None):
    print("clicked 4")
    file = audio_path + "/Help.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(3)


def B5(channel=None):
    print("clicked 5")
    file = audio_path + "/hug.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(3)


def B6(channel=None):
    print("clicked 6")
    file = audio_path + "/Hungry.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(3)

def B7a(channel=None):
    print("clicked 7")
    file = audio_path + "/Play.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(3)

def B7b(channel=None):
    file = audio_path + "/Pause.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(3)

def B8(channel=None):
    print("clicked 8")
    file = audio_path + "/Skip.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(3)

if __name__ == '__main__':
    say_play()
