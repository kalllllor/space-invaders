import pygame


class Bullet:
    def __init__(self, x, y, direction):
        self.bullet_icon = pygame.image.load("./Assets/bullet.png")
        self.bulletX = x
        self.bulletY = y
        self.bulletY_change = 1
        self.bullet_flag = False
        self.bullet_direction = direction

    def update(self, screen):
        screen.blit(self.bullet_icon, (self.bulletX + 24, self.bulletY - 15))
