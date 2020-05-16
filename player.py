import pygame
import bullet


class Player:
    def __init__(self):
        self.player_icon = pygame.image.load("./Assets/player.png")
        self.playerX = 468
        self.playerY = 268
        self.playerX_change = 0
        self.playerY_change = 0

    def update(self, screen, keys):
        screen.blit(self.player_icon, (self.playerX, self.playerY))
        if keys[pygame.K_LEFT]:
            self.playerX_change = -1
        elif keys[pygame.K_RIGHT]:
            self.playerX_change = 1
        else:
            self.playerX_change = 0
        self.playerX += self.playerX_change
        if self.playerX >= 936:
            self.playerX = 936
        elif self.playerX <= 0:
            self.playerX = 0

     def shot(self, keys):
         if keys[pygame.K_SPACE]:
             bullet1 = bullet.Bullet(self.playerX + 24, self.playerY - 15)
            return bullet1
         else:
            return None
