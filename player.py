import pygame


class Player:
    def __init__(self):
        self.player_icon = pygame.image.load("./Assets/player.png")
        self.playerX = 468
        self.playerY = 268
        self.playerX_change = 0
        self.playerY_change = 0

    def update(self, screen):
        screen.blit(self.player_icon, (self.playerX, self.playerY))
