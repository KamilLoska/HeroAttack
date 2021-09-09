import pygame
from pygame.sprite import Sprite
import sys
import os


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


class hero(Sprite):
    def __init__(self, screen):
        super(hero, self).__init__()

        self.screen = screen
        self.hero = hero
        self.image = pygame.image.load(resource_path('hero3.png')).convert_alpha()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # set rect of object on right site of screen
        self.rect.bottomleft = self.screen_rect.bottomleft
        # self.x = float(self.rect.centerx)
        self.x = float(self.rect.centerx)
        self.rect.y -= 32
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # Przesunięcie obcego na górę i dół
        #if self.moving_right and self.rect.right < self.screen_rect.right:
         #   self.rect.centerx += 1
        #if self.moving_left and self.rect.left > 0:
         #   self.rect.centerx -= 1
        #self.rect.centery = self.center
        self.rect.x = self.x


    #def draw_hero(self):
     #   pygame.draw.rect(self.screen, (230,230,230), self.rect)


   # def check_edges(self):
        # Zwraca wartość True, jeśłi obcy znajduje się przy krawędzi ekranu.
    #    screen_rect = self.screen.get_rect()
     #   if self.rect.left <= screen_rect.left:
      #      return True
       # elif self.rect.right >= screen_rect.right:
        #    return True
