import pygame
import sys
import time
import random
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode([3840,2160])

pygame.display.set_caption("BLOCKS DODGE")

clock = pygame.time.Clock()

welcomeScreen = pygame.image.load("assets/images/welcomeScreen.png")
screen1 = pygame.image.load("assets/images/screen1.png")
screen2 = pygame.image.load("assets/images/screen2.png")


font = pygame.font.SysFont(None, 45)
font2 = pygame.font.SysFont(None, 35)
font3 = pygame.font.SysFont(None, 95)

player_width = 50
player_height = 100
player_speed = 5

player2_width = 50
player2_height = 100
player2_speed = 5

obstacle_width = 100
obstacle_height = 50
obstacle2_width = 100
obstacle2_height = 50
obstacle3_width = 100
obstacle3_height = 50
obstacle4_width = 100
obstacle4_height = 50
obstacle5_width = 100
obstacle5_height = 50
obstacle5_width = 100
obstacle6_height = 50
obstacle7_width = 100
obstacle7_height = 50


topBorder = pygame.draw.rect(screen, (0,0,0), (0,555,3840,1),0)
bottomBorder = pygame.draw.rect(screen, (0,0,0), (0,1659,3840,1),0)
leftBorder = pygame.draw.rect(screen, (0,0,0), (1000,0,1,2160), 0)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

startfenster = True

while True:
    if startfenster:
        pygame.mixer.music.load('assets/sounds/playingSound.mp3')
        pygame.mixer.music.play(-1,0.0)

        while startfenster:
            screen.fill((255,255,255))
            screen.blit(welcomeScreen, (1000, 500))
            draw_text('Press any button to continue', font, (0, 0, 0), screen, 1625, 1500)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    startfenster = False

            pygame.display.update()
            clock.tick(60)        


    screen.fill((255,255,255))
    screen.blit(screen1, (1000, 500))

 
    mx, my = pygame.mouse.get_pos()
 
    button_1 = pygame.Rect(1000, 1200, 200, 50)
    button_2 = pygame.Rect(1000, 1300, 200, 50)
    button_3 = pygame.Rect(1000, 1400, 200, 50)
    button_4 = pygame.Rect(1000, 1500, 200, 50)
        
    if button_1.collidepoint((mx, my)):
        if click:
            player_x = 1920
            player_y = 1080
            player_speed = 5
            player_points = 0
            player_alive = True

            obstacle_x = 3840
            obstacle_y = random.randint(525,1609)
            obstacle_speed = random.randint(10,15)
            obstacle_red = random.randint(0,255)
            obstacle_yellow = random.randint(0,254)
            obstacle_blue = random.randint(0,255)

            obstacle2_x = 3840
            obstacle2_y = random.randint(525,1609)
            obstacle2_speed = random.randint(10,15)
            obstacle2_red = random.randint(0,255)
            obstacle2_yellow = random.randint(0,254)
            obstacle2_blue = random.randint(0,255)
            
            obstacle3_x = 3840
            obstacle3_y = random.randint(525,1609)
            obstacle3_speed = random.randint(10,15)
            obstacle3_red = random.randint(0,255)
            obstacle3_yellow = random.randint(0,254)
            obstacle3_blue = random.randint(0,255)

            obstacle4_x = 3840
            obstacle4_y = random.randint(525,1609)
            obstacle4_speed = random.randint(10,15)
            obstacle4_red = random.randint(0,255)
            obstacle4_yellow = random.randint(0,254)
            obstacle4_blue = random.randint(0,255)

            obstacle5_x = 3840
            obstacle5_y = random.randint(525,1609)
            obstacle5_speed = random.randint(10,15)
            obstacle5_red = random.randint(0,255)
            obstacle5_yellow = random.randint(0,254)
            obstacle5_blue = random.randint(0,255)

            obstacle6_x = 3840
            obstacle6_y = random.randint(525,1609)
            obstacle6_speed = random.randint(10,15)
            obstacle6_red = random.randint(0,255)
            obstacle6_yellow = random.randint(0,254)
            obstacle6_blue = random.randint(0,255)

            obstacle7_x = 3840
            obstacle7_y = random.randint(525,1609)
            obstacle7_speed = random.randint(10,15)
            obstacle7_red = random.randint(0,255)
            obstacle7_yellow = random.randint(0,254)
            obstacle7_blue = random.randint(0,255)

            gameover_sound = pygame.mixer.Sound('assets/sounds/gameoverSound.mp3')

            gamerunning = True
            gameover_sound_play = True
            gamepaused = False
            gamestop = False

            while gamerunning:
                screen.fill((255,255,255))
                if gamestop:
                    gamerunning = False
                if gamepaused:
                    while gamepaused:
                        screen.fill((255,255,255))
                        screen.blit(screen2, (1000, 500))

                        mx, my = pygame.mouse.get_pos()

                        button_1 = pygame.Rect(1000, 600, 200, 50)
                        button_2 = pygame.Rect(1000, 700, 200, 50)
                        button_3 = pygame.Rect(1000, 800, 200, 50)

                        if button_1.collidepoint((mx, my)):
                            if click:
                                gamepaused = False

                        if button_2.collidepoint((mx, my)):
                            if click:
                                gamepaused = False
                                gamestop = True

                        if button_3.collidepoint((mx, my)):
                            if click:
                                pygame.quit()
                                sys.exit()
                            
                        
                        pygame.draw.rect(screen, (255, 255, 255), button_1)
                        pygame.draw.rect(screen, (255, 255, 255), button_2)
                        pygame.draw.rect(screen, (255, 255, 255), button_3)

                        draw_text('Paused', font, (0, 0, 0), screen, 1000, 500)
                        draw_text('Continue', font, (0, 0, 0), screen, 1000, 600)
                        draw_text('Main menu', font, (0, 0, 0), screen, 1000, 700)
                        draw_text('Exit', font, (0, 0, 0), screen, 1000, 800)

                        click = False
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                pygame.quit()
                                sys.exit()
                            if event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                    gamepaused = False
                                    pygame.mixer.music.play(-1,0.0)

                            if event.type == MOUSEBUTTONDOWN:
                                if event.button == 1:
                                    click = True
 
                        pygame.display.update()
                        clock.tick(60)

                points_display = font3.render(str(player_points), 1, (0,0,0))
                if player_alive == True:
                    screen.blit(points_display, (1920, 500))
                
                player = pygame.Rect(player_x,player_y,player_width,player_height)

                obstacle = pygame.Rect(obstacle_x,obstacle_y,obstacle_width,obstacle_height)
                obstacle2 = pygame.Rect(obstacle2_x,obstacle2_y,obstacle2_width,obstacle2_height)
                obstacle3 = pygame.Rect(obstacle3_x,obstacle3_y,obstacle3_width,obstacle3_height)
                obstacle4 = pygame.Rect(obstacle4_x,obstacle4_y,obstacle4_width,obstacle4_height)
                obstacle5 = pygame.Rect(obstacle5_x,obstacle5_y,obstacle5_width,obstacle5_height)
                obstacle6 = pygame.Rect(obstacle6_x,obstacle6_y,obstacle5_width,obstacle6_height)
                obstacle7 = pygame.Rect(obstacle7_x,obstacle7_y,obstacle7_width,obstacle7_height)


                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE and not player_alive == False:
                            gamepaused = True
                        if event.key == K_ESCAPE and player_alive == False:
                            gamerunning = False
                            pygame.mixer.music.load('assets/sounds/playingSound.mp3')
                            pygame.mixer.music.play(-1,0.0)
                
                if player_alive == False:
                    if gameover_sound_play:
                        pygame.mixer.music.pause()
                        pygame.mixer.Sound.play(gameover_sound)
                    screen.blit(screen1, (1000, 500))
                    draw_text('GAMEOVER', font3, (0, 0, 0), screen, 1750, 1000)
                    screen.blit(points_display, (1920, 1250))
                    player_y = 5000
                    player_speed = 0
                    obstacle_y = 5000
                    obstacle2_y = 5000
                    obstacle3_y = 5000
                    obstacle4_y = 5000
                    obstacle5_y = 5000
                    obstacle6_y = 5000
                    obstacle7_y = 5000
                    obstacle_speed = 0
                    obstacle2_speed = 0
                    obstacle3_speed = 0
                    obstacle4_speed = 0
                    obstacle5_speed = 0
                    obstacle6_speed = 0
                    obstacle7_speed = 0
                    gameover_sound_play = False

                button_pressed = pygame.key.get_pressed()

                if button_pressed[pygame.K_w] and not player.colliderect(topBorder):
                    player_y -= player_speed 
                if button_pressed[pygame.K_s] and not player.colliderect(bottomBorder):
                    player_y += player_speed

                obstacle_x -= obstacle_speed
                obstacle2_x -= obstacle2_speed
                obstacle3_x -= obstacle3_speed
                obstacle4_x -= obstacle4_speed
                obstacle5_x -= obstacle5_speed
                obstacle6_x -= obstacle6_speed
                obstacle7_x -= obstacle6_speed

                                
                if obstacle.colliderect(leftBorder):
                    obstacle_x = 3840
                    obstacle_y = random.randint(525,1609)
                    obstacle_speed = random.randint(10,15)
                    obstacle_red = random.randint(0,255)
                    obstacle_yellow = random.randint(0,254)
                    obstacle_blue = random.randint(0,255)
                    player_points += 1
                    
                if obstacle2.colliderect(leftBorder):
                    obstacle2_x = 3840
                    obstacle2_y = random.randint(525,1609)
                    obstacle2_speed = random.randint(10,15)
                    obstacle2_red = random.randint(0,255)
                    obstacle2_yellow = random.randint(0,254)
                    obstacle2_blue = random.randint(0,255)
                    player_points += 1
                
                if obstacle3.colliderect(leftBorder):
                    obstacle3_x = 3840
                    obstacle3_y = random.randint(525,1609)
                    obstacle3_speed = random.randint(10,15)
                    obstacle3_red = random.randint(0,255)
                    obstacle3_yellow = random.randint(0,254)
                    obstacle3_blue = random.randint(0,255)
                    player_points += 1
                
                if obstacle4.colliderect(leftBorder):
                    obstacle4_x = 3840
                    obstacle4_y = random.randint(525,1609)
                    obstacle4_speed = random.randint(10,15)
                    obstacle4_red = random.randint(0,255)
                    obstacle4_yellow = random.randint(0,254)
                    obstacle4_blue = random.randint(0,255)
                    player_points += 1
                
                if obstacle5.colliderect(leftBorder):
                    obstacle5_x = 3840
                    obstacle5_y = random.randint(525,1609)
                    obstacle5_speed = random.randint(10,15)
                    obstacle5_red = random.randint(0,255)
                    obstacle5_yellow = random.randint(0,254)
                    obstacle5_blue = random.randint(0,255)
                    player_points += 1
                
                if obstacle6.colliderect(leftBorder):
                    obstacle6_x = 3840
                    obstacle6_y = random.randint(525,1609)
                    obstacle6_speed = random.randint(10,15)
                    obstacle6_red = random.randint(0,255)
                    obstacle6_yellow = random.randint(0,254)
                    obstacle6_blue = random.randint(0,255)
                    player_points += 1
                
                if obstacle7.colliderect(leftBorder):
                    obstacle7_x = 3840
                    obstacle7_y = random.randint(525,1609)
                    obstacle7_speed = random.randint(10,15)
                    obstacle7_red = random.randint(0,255)
                    obstacle7_yellow = random.randint(0,254)
                    obstacle7_blue = random.randint(0,255)
                    player_points += 1
                
                if player.colliderect(obstacle):
                    obstacle_x = 3840
                    obstacle_y = random.randint(525,1609)
                    obstacle_speed = random.randint(10,15)
                    obstacle_red = random.randint(0,255)
                    obstacle_yellow = random.randint(0,254)
                    obstacle_blue = random.randint(0,255)
                    player_alive = False
                        

                if player.colliderect(obstacle2):
                    obstacle2_x = 3840
                    obstacle2_y = random.randint(525,1609)
                    obstacle2_speed = random.randint(10,15)
                    obstacle2_red = random.randint(0,255)
                    obstacle2_yellow = random.randint(0,254)
                    obstacle2_blue = random.randint(0,255)
                    player_alive = False
                    
        
                if player.colliderect(obstacle3):
                    obstacle3_x = 3840
                    obstacle3_y = random.randint(525,1609)
                    obstacle3_speed = random.randint(10,15)
                    obstacle3_red = random.randint(0,255)
                    obstacle3_yellow = random.randint(0,254)
                    obstacle3_blue = random.randint(0,255)
                    player_alive = False
                
                if player.colliderect(obstacle4):
                    obstacle4_x = 3840
                    obstacle4_y = random.randint(525,1609)
                    obstacle4_speed = random.randint(10,15)
                    obstacle4_red = random.randint(0,255)
                    obstacle4_yellow = random.randint(0,254)
                    obstacle4_blue = random.randint(0,255)
                    player_alive = False
                
                if player.colliderect(obstacle5):
                    obstacle5_x = 3840
                    obstacle5_y = random.randint(525,1609)
                    obstacle5_speed = random.randint(10,15)
                    obstacle5_red = random.randint(0,255)
                    obstacle5_yellow = random.randint(0,254)
                    obstacle5_blue = random.randint(0,255)
                    player_alive = False
                
                if player.colliderect(obstacle6):
                    obstacle6_x = 3840
                    obstacle6_y = random.randint(525,1609)
                    obstacle6_speed = random.randint(10,15)
                    obstacle6_red = random.randint(0,255)
                    obstacle6_yellow = random.randint(0,254)
                    obstacle6_blue = random.randint(0,255)
                    player_alive = False
                
                if player.colliderect(obstacle7):
                    obstacle7_x = 3840
                    obstacle7_y = random.randint(525,1609)
                    obstacle7_speed = random.randint(10,15)
                    obstacle7_red = random.randint(0,255)
                    obstacle7_yellow = random.randint(0,254)
                    obstacle7_blue = random.randint(0,255)
                    player_alive = False
                
                pygame.draw.rect(screen, (0, 255, 0), player)

                pygame.draw.rect(screen, (obstacle_red,obstacle_yellow,obstacle_blue), obstacle)
                pygame.draw.rect(screen, (obstacle2_red,obstacle2_yellow,obstacle2_blue), obstacle2)
                pygame.draw.rect(screen, (obstacle3_red,obstacle3_yellow,obstacle3_blue), obstacle3)
                pygame.draw.rect(screen, (obstacle4_red,obstacle4_yellow,obstacle4_blue), obstacle4)
                pygame.draw.rect(screen, (obstacle5_red,obstacle5_yellow,obstacle4_blue), obstacle5)
                pygame.draw.rect(screen, (obstacle6_red,obstacle6_yellow,obstacle6_blue), obstacle6)
                pygame.draw.rect(screen, (obstacle7_red,obstacle7_yellow,obstacle7_blue), obstacle7)

                pygame.display.update()
                clock.tick(60)
            
    if button_2.collidepoint((mx, my)):
        if click:
            player_x = 1920
            player_y = 1000
            player_speed = 5
            player_points = 0
            player_alive = True

            player2_x = 1920
            player2_y = 1160
            player2_speed = 5
            player2_points = 0
            player2_alive = True

            obstacle_x = 3840
            obstacle_y = random.randint(525,1609)
            obstacle_speed = random.randint(10,15)
            obstacle_red = random.randint(0,255)
            obstacle_yellow = random.randint(0,255)
            obstacle_blue = random.randint(0,255)

            obstacle2_x = 3840
            obstacle2_y = random.randint(525,1609)
            obstacle2_speed = random.randint(10,15)
            obstacle2_red = random.randint(0,255)
            obstacle2_yellow = random.randint(0,255)
            obstacle2_blue = random.randint(0,255)
            
            obstacle3_x = 3840
            obstacle3_y = random.randint(525,1609)
            obstacle3_speed = random.randint(10,15)
            obstacle3_red = random.randint(0,255)
            obstacle3_yellow = random.randint(0,255)
            obstacle3_blue = random.randint(0,255)

            obstacle4_x = 3840
            obstacle4_y = random.randint(525,1609)
            obstacle4_speed = random.randint(10,15)
            obstacle4_red = random.randint(0,255)
            obstacle4_yellow = random.randint(0,255)
            obstacle4_blue = random.randint(0,255)

            obstacle5_x = 3840
            obstacle5_y = random.randint(525,1609)
            obstacle5_speed = random.randint(10,15)
            obstacle5_red = random.randint(0,255)
            obstacle5_yellow = random.randint(0,255)
            obstacle5_blue = random.randint(0,255)

            obstacle6_x = 3840
            obstacle6_y = random.randint(525,1609)
            obstacle6_speed = random.randint(10,15)
            obstacle6_red = random.randint(0,255)
            obstacle6_yellow = random.randint(0,255)
            obstacle6_blue = random.randint(0,255)

            obstacle7_x = 3840
            obstacle7_y = random.randint(525,1609)
            obstacle7_speed = random.randint(10,15)
            obstacle7_red = random.randint(0,255)
            obstacle7_yellow = random.randint(0,255)
            obstacle7_blue = random.randint(0,255)

            gameover_sound = pygame.mixer.Sound('assets/sounds/gameoverSound.mp3')

            gamerunning = True
            gameover_sound_play = True
            gamepaused = False
            gamestop = False

            while gamerunning:
                screen.fill((255,255,255))
                if gamestop:
                    gamerunning = False
                if gamepaused:
                    while gamepaused:
                        screen.fill((255,255,255))
                        screen.blit(screen2, (1000, 500))

                        mx, my = pygame.mouse.get_pos()

                        button_1 = pygame.Rect(1000, 600, 200, 50)
                        button_2 = pygame.Rect(1000, 700, 200, 50)
                        button_3 = pygame.Rect(1000, 800, 200, 50)

                        if button_1.collidepoint((mx, my)):
                            if click:
                                gamepaused = False

                        if button_2.collidepoint((mx, my)):
                            if click:
                                gamepaused = False
                                gamestop = True

                        if button_3.collidepoint((mx, my)):
                            if click:
                                pygame.quit()
                                sys.exit()
                            
                        
                        pygame.draw.rect(screen, (255, 255, 255), button_1)
                        pygame.draw.rect(screen, (255, 255, 255), button_2)
                        pygame.draw.rect(screen, (255, 255, 255), button_3)

                        draw_text('Paused', font, (0, 0, 0), screen, 1000, 500)
                        draw_text('Continue', font, (0, 0, 0), screen, 1000, 600)
                        draw_text('Main Menu', font, (0, 0, 0), screen, 1000, 700)
                        draw_text('Exit', font, (0, 0, 0), screen, 1000, 800)

                        click = False
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                pygame.quit()
                                sys.exit()
                            if event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                    gamepaused = False
                                    pygame.mixer.music.play(-1,0.0)

                            if event.type == MOUSEBUTTONDOWN:
                                if event.button == 1:
                                    click = True
 
                        pygame.display.update()
                        clock.tick(60)

                points_display = font3.render(str(player_points), 1, (0,0,0))
                if player_alive == True:
                    screen.blit(points_display, (1920, 500))
                
                player = pygame.Rect(player_x,player_y,player_width,player_height)
                player2 = pygame.Rect(player2_x,player2_y,player2_width,player2_height)

                obstacle = pygame.Rect(obstacle_x,obstacle_y,obstacle_width,obstacle_height)
                obstacle2 = pygame.Rect(obstacle2_x,obstacle2_y,obstacle2_width,obstacle2_height)
                obstacle3 = pygame.Rect(obstacle3_x,obstacle3_y,obstacle3_width,obstacle3_height)
                obstacle4 = pygame.Rect(obstacle4_x,obstacle4_y,obstacle4_width,obstacle4_height)
                obstacle5 = pygame.Rect(obstacle5_x,obstacle5_y,obstacle5_width,obstacle5_height)
                obstacle6 = pygame.Rect(obstacle6_x,obstacle6_y,obstacle5_width,obstacle6_height)
                obstacle7 = pygame.Rect(obstacle7_x,obstacle7_y,obstacle7_width,obstacle7_height)


                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE and not player_alive == False:
                            gamepaused = True
                        if event.key == K_ESCAPE and player_alive == False:
                            gamerunning = False
                            pygame.mixer.music.load('assets/sounds/playingSound.mp3')
                            pygame.mixer.music.play(-1,0.0)
                        if event.key == K_ESCAPE and player2_alive == False:
                            gamerunning = False
                            pygame.mixer.music.load('assets/sounds/playingSound.mp3')
                            pygame.mixer.music.play(-1,0.0)
                
                if player_alive == False:
                    if gameover_sound_play:
                        pygame.mixer.music.pause()
                        pygame.mixer.Sound.play(gameover_sound)
                    screen.blit(screen1, (1000, 500))
                    draw_text('WON', font3, (0, 0, 255), screen, 2250, 1000)
                    draw_text('GAMEOVER', font3, (0, 255, 0), screen, 1250, 1000)
                    screen.blit(points_display, (1920, 1250))
                    player_y = 5000
                    player2_y = 5000
                    player_speed = 0
                    obstacle_y = 5000
                    obstacle2_y = 5000
                    obstacle3_y = 5000
                    obstacle4_y = 5000
                    obstacle5_y = 5000
                    obstacle6_y = 5000
                    obstacle7_y = 5000
                    obstacle_speed = 0
                    obstacle2_speed = 0
                    obstacle3_speed = 0
                    obstacle4_speed = 0
                    obstacle5_speed = 0
                    obstacle6_speed = 0
                    obstacle7_speed = 0
                    gameover_sound_play = False

                if player2_alive == False:
                    if gameover_sound_play:
                        pygame.mixer.music.pause()
                        pygame.mixer.Sound.play(gameover_sound)
                    screen.blit(screen1, (1000, 500))
                    draw_text('WON', font3, (0, 255, 0), screen, 1250, 1000)
                    draw_text('GAMEOVER', font3, (0, 0, 255), screen, 2250, 1000)
                    screen.blit(points_display, (1920, 1250))
                    player_y = 5000
                    player2_y = 5000
                    player_speed = 0
                    obstacle_y = 5000
                    obstacle2_y = 5000
                    obstacle3_y = 5000
                    obstacle4_y = 5000
                    obstacle5_y = 5000
                    obstacle6_y = 5000
                    obstacle7_y = 5000
                    obstacle_speed = 0
                    obstacle2_speed = 0
                    obstacle3_speed = 0
                    obstacle4_speed = 0
                    obstacle5_speed = 0
                    obstacle6_speed = 0
                    obstacle7_speed = 0
                    gameover_sound_play = False

                button_pressed = pygame.key.get_pressed()

                if button_pressed[pygame.K_w] and not player.colliderect(topBorder):
                    player_y -= player_speed 
                if button_pressed[pygame.K_s] and not player.colliderect(bottomBorder):
                    player_y += player_speed

                if button_pressed[pygame.K_UP] and not player2.colliderect(topBorder):
                    player2_y -= player2_speed 
                if button_pressed[pygame.K_DOWN] and not player2.colliderect(bottomBorder):
                    player2_y += player2_speed

                obstacle_x -= obstacle_speed
                obstacle2_x -= obstacle2_speed
                obstacle3_x -= obstacle3_speed
                obstacle4_x -= obstacle4_speed
                obstacle5_x -= obstacle5_speed
                obstacle6_x -= obstacle6_speed
                obstacle7_x -= obstacle6_speed

                                
                if obstacle.colliderect(leftBorder):
                    obstacle_x = 3840
                    obstacle_y = random.randint(525,1609)
                    obstacle_speed = random.randint(10,15)
                    obstacle_red = random.randint(0,255)
                    obstacle_yellow = random.randint(0,255)
                    obstacle_blue = random.randint(0,255)
                    player_points += 1
                    
                if obstacle2.colliderect(leftBorder):
                    obstacle2_x = 3840
                    obstacle2_y = random.randint(525,1609)
                    obstacle2_speed = random.randint(10,15)
                    obstacle2_red = random.randint(0,255)
                    obstacle2_yellow = random.randint(0,255)
                    obstacle2_blue = random.randint(0,255)
                    player_points += 1
                
                if obstacle3.colliderect(leftBorder):
                    obstacle3_x = 3840
                    obstacle3_y = random.randint(525,1609)
                    obstacle3_speed = random.randint(10,15)
                    obstacle3_red = random.randint(0,255)
                    obstacle3_yellow = random.randint(0,255)
                    obstacle3_blue = random.randint(0,255)
                    player_points += 1
                
                if obstacle4.colliderect(leftBorder):
                    obstacle4_x = 3840
                    obstacle4_y = random.randint(525,1609)
                    obstacle4_speed = random.randint(10,15)
                    obstacle4_red = random.randint(0,255)
                    obstacle4_yellow = random.randint(0,255)
                    obstacle4_blue = random.randint(0,255)
                    player_points += 1
                
                if obstacle5.colliderect(leftBorder):
                    obstacle5_x = 3840
                    obstacle5_y = random.randint(525,1609)
                    obstacle5_speed = random.randint(10,15)
                    obstacle5_red = random.randint(0,255)
                    obstacle5_yellow = random.randint(0,255)
                    obstacle5_blue = random.randint(0,255)
                    player_points += 1
                
                if obstacle6.colliderect(leftBorder):
                    obstacle6_x = 3840
                    obstacle6_y = random.randint(525,1609)
                    obstacle6_speed = random.randint(10,15)
                    obstacle6_red = random.randint(0,255)
                    obstacle6_yellow = random.randint(0,255)
                    obstacle6_blue = random.randint(0,255)
                    player_points += 1
                
                if obstacle7.colliderect(leftBorder):
                    obstacle7_x = 3840
                    obstacle7_y = random.randint(525,1609)
                    obstacle7_speed = random.randint(10,15)
                    obstacle7_red = random.randint(0,255)
                    obstacle7_yellow = random.randint(0,255)
                    obstacle7_blue = random.randint(0,255)
                    player_points += 1
                
                if player.colliderect(obstacle):
                    obstacle_x = 3840
                    obstacle_y = random.randint(525,1609)
                    obstacle_speed = random.randint(10,15)
                    obstacle_red = random.randint(0,255)
                    obstacle_yellow = random.randint(0,255)
                    obstacle_blue = random.randint(0,255)
                    player_alive = False
                        

                if player.colliderect(obstacle2):
                    obstacle2_x = 3840
                    obstacle2_y = random.randint(525,1609)
                    obstacle2_speed = random.randint(10,15)
                    obstacle2_red = random.randint(0,255)
                    obstacle2_yellow = random.randint(0,255)
                    obstacle2_blue = random.randint(0,255)
                    player_alive = False
                    
        
                if player.colliderect(obstacle3):
                    obstacle3_x = 3840
                    obstacle3_y = random.randint(525,1609)
                    obstacle3_speed = random.randint(10,15)
                    obstacle3_red = random.randint(0,255)
                    obstacle3_yellow = random.randint(0,255)
                    obstacle3_blue = random.randint(0,255)
                    player_alive = False
                
                if player.colliderect(obstacle4):
                    obstacle4_x = 3840
                    obstacle4_y = random.randint(525,1609)
                    obstacle4_speed = random.randint(10,15)
                    obstacle4_red = random.randint(0,255)
                    obstacle4_yellow = random.randint(0,255)
                    obstacle4_blue = random.randint(0,255)
                    player_alive = False
                
                if player.colliderect(obstacle5):
                    obstacle5_x = 3840
                    obstacle5_y = random.randint(525,1609)
                    obstacle5_speed = random.randint(10,15)
                    obstacle5_red = random.randint(0,255)
                    obstacle5_yellow = random.randint(0,255)
                    obstacle5_blue = random.randint(0,255)
                    player_alive = False
                
                if player.colliderect(obstacle6):
                    obstacle6_x = 3840
                    obstacle6_y = random.randint(525,1609)
                    obstacle6_speed = random.randint(10,15)
                    obstacle6_red = random.randint(0,255)
                    obstacle6_yellow = random.randint(0,255)
                    obstacle6_blue = random.randint(0,255)
                    player_alive = False
                
                if player.colliderect(obstacle7):
                    obstacle7_x = 3840
                    obstacle7_y = random.randint(525,1609)
                    obstacle7_speed = random.randint(10,15)
                    obstacle7_red = random.randint(0,255)
                    obstacle7_yellow = random.randint(0,255)
                    obstacle7_blue = random.randint(0,255)
                    player_alive = False
                
                if player2.colliderect(obstacle):
                    obstacle_x = 3840
                    obstacle_y = random.randint(525,1609)
                    obstacle_speed = random.randint(10,15)
                    obstacle_red = random.randint(0,255)
                    obstacle_yellow = random.randint(0,255)
                    obstacle_blue = random.randint(0,255)
                    player2_alive = False
                        

                if player2.colliderect(obstacle2):
                    obstacle2_x = 3840
                    obstacle2_y = random.randint(525,1609)
                    obstacle2_speed = random.randint(10,15)
                    obstacle2_red = random.randint(0,255)
                    obstacle2_yellow = random.randint(0,255)
                    obstacle2_blue = random.randint(0,255)
                    player2_alive = False
                    
        
                if player2.colliderect(obstacle3):
                    obstacle3_x = 3840
                    obstacle3_y = random.randint(525,1609)
                    obstacle3_speed = random.randint(10,15)
                    obstacle3_red = random.randint(0,255)
                    obstacle3_yellow = random.randint(0,255)
                    obstacle3_blue = random.randint(0,255)
                    player2_alive = False
                
                if player2.colliderect(obstacle4):
                    obstacle4_x = 3840
                    obstacle4_y = random.randint(525,1609)
                    obstacle4_speed = random.randint(10,15)
                    obstacle4_red = random.randint(0,255)
                    obstacle4_yellow = random.randint(0,255)
                    obstacle4_blue = random.randint(0,255)
                    player2_alive = False
                
                if player2.colliderect(obstacle5):
                    obstacle5_x = 3840
                    obstacle5_y = random.randint(525,1609)
                    obstacle5_speed = random.randint(10,15)
                    obstacle5_red = random.randint(0,255)
                    obstacle5_yellow = random.randint(0,255)
                    obstacle5_blue = random.randint(0,255)
                    player2_alive = False
                
                if player2.colliderect(obstacle6):
                    obstacle6_x = 3840
                    obstacle6_y = random.randint(525,1609)
                    obstacle6_speed = random.randint(10,15)
                    obstacle6_red = random.randint(0,255)
                    obstacle6_yellow = random.randint(0,255)
                    obstacle6_blue = random.randint(0,255)
                    player2_alive = False
                
                if player2.colliderect(obstacle7):
                    obstacle7_x = 3840
                    obstacle7_y = random.randint(525,1609)
                    obstacle7_speed = random.randint(10,15)
                    obstacle7_red = random.randint(0,255)
                    obstacle7_yellow = random.randint(0,255)
                    obstacle7_blue = random.randint(0,255)
                    player2_alive = False
                
                pygame.draw.rect(screen, (0, 255, 0), player)
                pygame.draw.rect(screen, (0, 0, 255), player2)

                pygame.draw.rect(screen, (obstacle_red,obstacle_yellow,obstacle_blue), obstacle)
                pygame.draw.rect(screen, (obstacle2_red,obstacle2_yellow,obstacle2_blue), obstacle2)
                pygame.draw.rect(screen, (obstacle3_red,obstacle3_yellow,obstacle3_blue), obstacle3)
                pygame.draw.rect(screen, (obstacle4_red,obstacle4_yellow,obstacle4_blue), obstacle4)
                pygame.draw.rect(screen, (obstacle5_red,obstacle5_yellow,obstacle4_blue), obstacle5)
                pygame.draw.rect(screen, (obstacle6_red,obstacle6_yellow,obstacle6_blue), obstacle6)
                pygame.draw.rect(screen, (obstacle7_red,obstacle7_yellow,obstacle7_blue), obstacle7)

                pygame.display.update()
                clock.tick(60)
            

    if button_3.collidepoint((mx, my)):
        if click:
            instructionsrunning = True
            while instructionsrunning:
                screen.fill((255,255,255))

                screen.blit(screen2, (1000, 500))

                draw_text('Instructions:', font, (0, 0, 0), screen, 1000, 500)
                draw_text('Avoid the obstacles.', font, (0, 0, 0), screen, 1000, 600)
                draw_text('Use W to move up. (Green Player)', font, (0, 0, 0), screen, 1000, 700)
                draw_text('Use S to move down. (Green Player)', font, (0, 0, 0), screen, 1000, 800)
                draw_text('Use Arrow Up to move up. (Blue Player)', font, (0, 0, 0), screen, 1000, 900)
                draw_text('Use Arrow Down to move down. (Blue Player)', font, (0, 0, 0), screen, 1000, 1000)
                draw_text('Use Esc to open the main menu.', font, (0, 0, 0), screen, 1000, 1100)
                draw_text('Have fun!', font, (0, 0, 0), screen, 1000, 1200)
                
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            instructionsrunning = False
                
                pygame.display.update()
                clock.tick(60)


    if button_4.collidepoint((mx, my)):
        if click:
            pygame.quit()
            sys.exit()

    pygame.draw.rect(screen, (255, 255, 255), button_1)
    pygame.draw.rect(screen, (255, 255, 255), button_2)
    pygame.draw.rect(screen, (255, 255, 255), button_3)
    pygame.draw.rect(screen, (255, 255, 255), button_4)



    draw_text('Singelplayer', font, (0, 0, 0), screen, 1000, 1200)
    draw_text('Multiplayer', font, (0, 0, 0), screen, 1000, 1300)
    draw_text('Instructions', font, (0, 0, 0), screen, 1000, 1400)
    draw_text('Exit', font, (0, 0, 0), screen, 1000, 1500)
 
    click = False
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
 
    pygame.display.update()
    clock.tick(60)
