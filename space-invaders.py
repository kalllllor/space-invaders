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
text = pygame.font.Font('freesansbold.ttf', 50)

number_of_enemies = 6
start = 100

player1 = player.Player()
aliens = []
bullets = []
aliens_bullets = []
while len(aliens) < number_of_enemies:
    aliens.append(alien.Alien(start, 50))
    start += 146

def game_end(x, y):
    game_over = text.render('GAME OVER', True, (0, 0, 0))
    screen.blit(game_over, (x, y))

def win(x,y):
    game_over = text.render('YOU WIN :)))', True, (0, 0, 0))
    screen.blit(game_over, (x, y))

def collision(enemyX, enemyY, bulletX, bulletY):
    if(math.sqrt(math.pow(enemyX-bulletX, 2) + math.pow(enemyY-bulletY, 2))) < 32:
        return True
    else:
        return False

my_event = pygame.USEREVENT+1
pygame.time.set_timer(my_event, 1000)
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
        if collision(player1.playerX, player1.playerY, item.bulletX, item.bulletY):
            player1.health_point -= 1
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

    if player1.health_point <= 0:
        game_end(400, 300)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    running = False
            pygame.display.update()
    if len(aliens) == 0:
        win(400, 300)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    running = False
            pygame.display.update()

    print(player1.health_point)
    pygame.display.update()
    clock.tick(60)
