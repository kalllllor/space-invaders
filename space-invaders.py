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

    if player1.shot(keys_press):
        bullets.append(player1.shot(keys_press))

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

    for item in bullets:
        item.update(screen)
        for alien in aliens:
            if item.bulletY <= -16:
                bullets.remove(item)

            for alien in aliens:
                if collision(alien.alienX, alien.alienY, item.bulletX, item.bulletY):
                    alien.alien_hit = True
                    bullets.remove(item)

    print(bullets)
    pygame.display.update()
