import pygame
import math
pygame.init()


screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("SPACE INVADERS !!!ONE")
pygame.display.set_icon(pygame.image.load("./Assets/icon.png"))

# Player
player_icon = pygame.image.load("./Assets/player.png")
playerX = 468
playerY = 268
playerX_change = 0
playerY_change = 0

# Alien
alien_icon = pygame.image.load("./Assets/alien.png")
enemyX = 468
enemyY = 50
enemyX_change = 0.1
enemy_hit = False

# Bullet
bullet_icon = pygame.image.load("./Assets/bullet.png")
bulletX = 0
bulletY = 268
bulletY_change = 1
bullet_flag = False


def player(x, y):
    screen.blit(player_icon, (x, y))


def alien(x, y):
    screen.blit(alien_icon, (x, y))


def bullet(x, y):
    global bullet_flag
    bullet_flag = True
    screen.blit(bullet_icon, (x + 24, y - 15))


def collision(enemyX, enemyY, bulletX, bulletY):
    if(math.sqrt(math.pow(enemyX-bulletX, 2) + math.pow(enemyY-bulletY, 2))) < 32:
        return True
    else:
        return False


running = True
while running:

    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_SPACE:
                if not bullet_flag:
                    bullet_flag = True
                    bulletX = playerX
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX >= 936:
        playerX = 936
    elif playerX <= 0:
        playerX = 0

    enemyX += enemyX_change
    if enemyX >= 936:
        enemyX_change = -0.1
    elif enemyX <= 0:
        enemyX_change = 0.1

    if bullet_flag:
        bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    if bulletY <= -16:
        bullet_flag = False
        bulletY = 268
    player(playerX, playerY)

    if collision(enemyX+32, enemyY-32, bulletX, bulletY):
        enemy_hit = True
        bullet_flag = False

    if not enemy_hit:
        alien(enemyX, enemyY)

    pygame.display.update()
