import os
import ctypes
import pygame
from Application import Application

screen_size = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (screen_size[0] / 2 - 569, screen_size[1] / 2 - 320)
pygame.init()

if __name__ == "__main__":
    app = Application()
    app.Run()
