import pygame


class Bullet:
    def __init__(self, x, y, direction):
        if direction:
            self.bullet_icon = pygame.image.load("./Assets/bullet.png")
        else:
            self.bullet_icon = pygame.image.load("./Assets/alien_bullet.png")
        self.bulletX = x
        self.bulletY = y
        self.bulletY_change = 10
        self.bullet_flag = True
        self.bullet_direction = direction

    def update(self, screen):
        screen.blit(self.bullet_icon, (self.bulletX, self.bulletY))
        if self.bullet_direction:
            self.bulletY -= self.bulletY_change
        else:
            self.bulletY += self.bulletY_change
