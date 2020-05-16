import pygame


class Bullet:
    def __init__(self):
        self.bullet_icon = pygame.image.load("./Assets/bullet.png")
        self.bulletX = 0
        self.bulletY = 268
        self.bulletY_change = 1
        self.bullet_flag = False

    def update(self, screen):
        screen.blit(self.bullet_icon, (self.bulletX + 24, self.bulletY - 15))
