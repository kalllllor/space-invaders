import pygame
import math
import random
import player
import alien
import bullet
pygame.init()

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("SPACE INVADERS !!!ONE")
pygame.display.set_icon(pygame.image.load("./Assets/icon.png"))
clock = pygame.time.Clock()
bullets = []
number_of_enemies = 6
start = 100

player1 = player.Player()
aliens = []
while len(aliens) < number_of_enemies:
    aliens.append(alien.Alien(start, 50))
    start += 146
bullet1 = bullet.Bullet(0, 268, True)


def collision(enemyX, enemyY, bulletX, bulletY):
    if(math.sqrt(math.pow(enemyX-bulletX, 2) + math.pow(enemyY-bulletY, 2))) < 32:
        return True
    else:
        return False


running = True
while running:
    screen.fill((255, 255, 255))
    keys_press = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(player1.shot())

    # if bullet1.bulletY <= -16:
    #     bullet1.bullet_flag = False
    #     bullet1.bulletY = 268

    # for alien in aliens:
    #     if collision(alien.alienX, alien.alienY, bullet1.bulletX, bullet1.bulletY):
    #         alien.alien_hit = True
    #         bullet1.bullet_flag = False
    #         bullet1.bulletY = 268

    player1.update(screen, keys_press)

    for alien in aliens:
        if not alien.alien_hit:
            alien.update(screen)
        else:
            aliens.remove(alien)

    for item in bullets:
        if item.bullet_flag:
            item.update(screen)
        if item.bulletY <= -16:
            item.bullet_flag = False
        for alien in aliens:
            if collision(alien.alienX, alien.alienY, item.bulletX, item.bulletY):
                alien.alien_hit = True
                item.bullet_flag = False
        if not item.bullet_flag:
            bullets.remove(item)

    pygame.display.update()
    clock.tick(60)
