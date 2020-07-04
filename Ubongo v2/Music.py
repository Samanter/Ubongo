import pygame

def loadGameMusic():
    pygame.mixer.music.load("music/music_game.mp3")
    pygame.mixer.music.play(-1)

def loadMenuMusic():
    pygame.mixer.music.load("music/music_menu.mp3")
    pygame.mixer.music.play(-1)

def loadCheersMusic():
    pygame.mixer.music.load("music/music_cheers.mp3")
    pygame.mixer.music.play()
