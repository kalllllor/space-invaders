import pygame


class Alien:
    def __init__(self):
        self.alien_icon = pygame.image.load("./Assets/alien.png")
        self.alienX = 468
        self.alienY = 50
        self.alienX_change = 0.1
        self.alien_hit = False

    def update(self, screen):
        screen.blit(self.alien_icon, (self.alienX, self.alienY))
