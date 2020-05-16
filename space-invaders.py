import pygame
import math
import player
import alien
import bullet
pygame.init()

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("SPACE INVADERS !!!ONE")
pygame.display.set_icon(pygame.image.load("./Assets/icon.png"))


player1 = player.Player()
alien1 = alien.Alien()
bullet1 = bullet.Bullet()


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
                player1.playerX_change = -1
            if event.key == pygame.K_RIGHT:
                player1.playerX_change = 1
            if event.key == pygame.K_SPACE:
                if not bullet1.bullet_flag:
                    bullet1.bullet_flag = True
                    bullet1.bulletX = player1.playerX
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player1.playerX_change = 0

    player1.playerX += player1.playerX_change
    if player1.playerX >= 936:
        player1.playerX = 936
    elif player1.playerX <= 0:
        player1.playerX = 0

    alien1.alienX += alien1.alienX_change
    if alien1.alienX >= 936:
        alien1.alienX_change = -0.1
    elif alien1.alienX <= 0:
        alien1.alienX_change = 0.1

    if bullet1.bullet_flag:
        bullet1.update(screen)
        bullet1.bulletY -= bullet1.bulletY_change
    if bullet1.bulletY <= -16:
        bullet1.bullet_flag = False
        bullet1.bulletY = 268
    player1.update(screen)

    if collision(alien1.alienX, alien1.alienY, bullet1.bulletX, bullet1.bulletY):
        alien1.alien_hit = True
        bullet1.bullet_flag = False

    if not alien1.alien_hit:
        alien1.update(screen)

    pygame.display.update()
