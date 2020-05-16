import pygame


class Alien:
    def __init__(self, x, y):
        self.alien_icon = pygame.image.load("./Assets/alien.png")
        self.alienX = x
        self.alienY = y
        self.alienX_change = 1
        self.alienY_change = 20
        self.alien_hit = False

    def update(self, screen):
        screen.blit(self.alien_icon, (self.alienX, self.alienY))

        if self.alienX >= 936:
            self.alienX_change = -1
            self.alienY += self.alienY_change
        elif self.alienX <= 0:
            self.alienX_change = 1
            self.alienY += self.alienY_change
        self.alienX += self.alienX_change
