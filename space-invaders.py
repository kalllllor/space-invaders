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

number_of_enemies = 6
start = 100

player1 = player.Player()
aliens = []
bullets = []
aliens_bullets = []
while len(aliens) < number_of_enemies:
    aliens.append(alien.Alien(start, 50))
    start += 146


def collision(enemyX, enemyY, bulletX, bulletY):
    if(math.sqrt(math.pow(enemyX-bulletX, 2) + math.pow(enemyY-bulletY, 2))) < 32:
        return True
    else:
        return False


my_event = pygame.USEREVENT+1
pygame.time.set_timer(my_event, 500)
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
        if event.type == my_event:
            for alien in aliens:
                aliens_bullets.append(bullet.Bullet(alien.alienX + 32, alien.alienY + 32, False))

    player1.update(screen, keys_press)

    for alien in aliens:
        if not alien.alien_hit:
            alien.update(screen)
        else:
            aliens.remove(alien)

    for item in aliens_bullets:
        if item.bullet_flag:
            item.update(screen)
        if item.bulletY >= 616:
            item.bullet_flag = False
        if not item.bullet_flag:
            aliens_bullets.remove(item)

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
