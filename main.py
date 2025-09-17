import pygame
from pygame import mixer
import random
import asyncio

async def main():
    pygame.init()

    screen = pygame.display.set_mode((700,800))
    sky = pygame.image.load('assets/images/bluesky.png')
    pygame.display.set_caption('Aerial Fury')
    clock = pygame.time.Clock()

    mixer.music.load('assets/sounds/war_background.ogg')
    mixer.music.play(-1)
    mixer.music.set_volume(0.5)

    cover = pygame.image.load('assets/images/cover.png')

    #playerPlne
    player = pygame.image.load('assets/images/aircraft.png')
    playerX = 350
    playerY = 500
    def playerXY(x,y):
        screen.blit(player,(x,y))
    #playerVariable
    pX_change = 0


    #enemy
    enemy_images = [
        pygame.image.load('assets/images/jet1.png'),
        pygame.image.load('assets/images/jet2.png'),
        pygame.image.load('assets/images/jet3.png'),
        pygame.image.load('assets/images/jet4.png'),
        pygame.image.load('assets/images/jet5.png'),
        pygame.image.load('assets/images/jet6.png')
    ]


    #enemy1
    enmy1 = random.choice(enemy_images)
    enmy1X = 50
    enmy1Y = -100
    def enmy1XY(x,y):
        screen.blit(enmy1,(x,y))

    #enmy1_v
    enmy1_renew = 0
    enmy1_takeA = 0 #player bullet attack start position

    #enemyBullet
    b_enmy1X=enmy1X+30
    b_enmy1Y=30
    def b_enmy1XY(x,y):
        pygame.draw.line(screen,(255,0,0),(b_enmy1X,b_enmy1Y),(b_enmy1X,b_enmy1Y+10),5)

    #enemy2
    enmy2 = random.choice(enemy_images)
    enmy2X = 100
    enmy2Y = -200
    def enmy2XY(x,y):
        screen.blit(enmy2,(x,y))

    #enmy2_v
    enmy2_renew = 0
    enmy2_takeA = 0 #player bullet attack start position

    #enemyBullet
    b_enmy2X=enmy2X+30
    b_enmy2Y=30
    def b_enmy2XY(x,y):
        pygame.draw.line(screen,(255,0,0),(b_enmy2X,b_enmy2Y),(b_enmy2X,b_enmy2Y+10),5)



    #bullet
    bullet1X = playerX+30
    bullet2X = playerX+30
    bullet3X = playerX+30
    bullet4X = playerX+30
    bullet5X = playerX+30
    bullet6X = playerX+30
    bullet7X = playerX+30
    bullet8X = playerX+30
    bullet9X = playerX+30

    bullet1Y = 510
    bullet2Y = 570
    bullet3Y = 630
    bullet4Y = 690
    bullet5Y = 750
    bullet6Y = 810
    bullet7Y = 870
    bullet8Y = 930
    bullet9Y = 990

    #bulletV
    bullet_v1 = 0
    bullet_v2 = 0
    bullet_v3 = 0
    bullet_v4 = 0
    bullet_v5 = 0
    bullet_v6 = 0
    bullet_v7 = 0
    bullet_v8 = 0
    bullet_v9 = 0

    hbullet_v1 = 0
    hbullet_v2 = 0
    hbullet_v3 = 0
    hbullet_v4 = 0
    hbullet_v5 = 0
    hbullet_v6 = 0
    hbullet_v7 = 0
    hbullet_v8 = 0
    hbullet_v9 = 0 #bullet hide variable

    change_bulletY = 5 #player bullet speed change

    #health
    hfont = pygame.font.SysFont('freesansbold.ttf',40)
    health_value = 100
    def healthXY(x,y,health_value):
        pygame.draw.line(screen, (0, 0, 0), (x, y), (x+200, y), 30) #darkline
        pygame.draw.line(screen,(215-health_value*2,health_value*2,0),(x,y),(x+2*health_value,y),30)
        health=hfont.render(str(health_value)+"%",True,(0,245,0))
        screen.blit(health,(x-84,y-10))
    #score
    scoreX=20
    scoreY = 560
    sfont = pygame.font.SysFont('freesansbold.ttf',64)
    score_value = 0
    def scoreXY(x,y):
        score = sfont.render('SCORE:'+str(score_value),True,(255,0,0))
        screen.blit(score,(x,y))

    #gameOver
    gameOver = False
    gfont = pygame.font.SysFont('freesansbold.ttf',128)
    def gameXY(x,y):
        game = gfont.render('GAME OVER',True,(0,0,0))
        screen.blit(game,(x,y))

    #music on off variable
    gSoundOn = 0
    game_start = False

    # user interface
    gameStart_0 = False
    button_start = pygame.Rect(200, 690, 250, 80)
    button_pad = pygame.Rect(0, 600, 700, 200)  # x,y,w,h
    button_left = pygame.Rect(40, 640, 140, 100)
    button_right = pygame.Rect(520, 640, 140, 100)
    button_continue = pygame.Rect(200, 640, 270, 80)

    font_btn= pygame.font.SysFont('freesansbold.ttf', 64)

    def draw_start_button():
        pygame.draw.rect(screen, (10, 200, 10), button_start, border_radius=20)
        text = font_btn.render("START", True, (0, 0, 0))
        screen.blit(text, (button_start.x + 50, button_start.y + 20))
    def draw_button_pad():
        pygame.draw.rect(screen, (200, 150, 200), button_pad)
    def draw_buttons():
        pygame.draw.rect(screen, (100, 100, 100), button_left, border_radius= 20)
        text = font_btn.render("<<", True, (0, 0, 0))
        screen.blit(text, (button_left.x + 30, button_left.y + 20))

        pygame.draw.rect(screen, (100, 100, 100), button_right, border_radius=20)
        text = font_btn.render(">>", True, (0, 0, 0))
        screen.blit(text, (button_right.x + 35, button_right.y + 20))

    def draw_continue_button():
        pygame.draw.rect(screen, (250, 100, 10), button_continue, border_radius=30)
        text = font_btn.render("Continue", True, (0, 0, 0))
        screen.blit(text, (button_continue.x + 40, button_continue.y + 20))




    running = True
    while running:
        screen.fill((0,0,0))
        screen.blit(sky,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    pX_change +=4 #change
                if event.key == pygame.K_LEFT:
                    pX_change -=4 #change
                if event.key == pygame.K_UP and game_start == False:
                    game_start = True
                if event.key == pygame.K_SPACE and gameOver == True : #restart_game
                    gameOver = False
                    score_value=0
                    health_value=100
                    gSoundOn = 0
                    gmoverS.stop()
                    mixer.music.play(-1)
                    #restart_game
            if event.type == pygame.KEYUP:
                pX_change = 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_start.collidepoint(event.pos) and game_start == False:
                    game_start = True
                if button_right.collidepoint(event.pos):
                    pX_change +=4 #change
                if button_left.collidepoint(event.pos):
                    pX_change -= 4  # change
                if button_continue.collidepoint(event.pos) and gameOver == True:
                    gameOver = False
                    game_start = False
                    score_value = 0
                    health_value = 100
                    gSoundOn = 0
                    gmoverS.stop()
                    mixer.music.play(-1)
                    # restart_game
            if event.type == pygame.MOUSEBUTTONUP:
                pX_change = 0


        if gameOver == False and game_start == True :
            #bullet1
            if bullet1Y >= 500:
                bullet_v1 = 0
            else:
                bullet_v1=2

            if bullet_v1 == 0:
                bullet1X = playerX + 30
            if bullet_v1 == 2:
                bullet1X = bullet1X
            bullet1Y -= change_bulletY
            if bullet1Y <= -6:
                bullet1Y = 510
                bullet_v1 = 0
            if bullet1Y<=510 and bullet_v1 == 2:
                pygame.draw.line(screen,(0,0,0),(bullet1X,bullet1Y),(bullet1X,bullet1Y+10),7)

            # bullet2
            if bullet2Y >= 500:
                bullet_v2 = 0
            else:
                bullet_v2 = 2

            if bullet_v2 == 0:
                bullet2X = playerX + 30
            if bullet_v2 == 2:
                bullet2X = bullet2X
            bullet2Y -= change_bulletY
            if bullet2Y <= -6:
                bullet2Y = 510
                bullet_v2 = 0
            if bullet2Y <= 510 and bullet_v2 == 2:
                pygame.draw.line(screen, (0, 0, 0), (bullet2X, bullet2Y), (bullet2X, bullet2Y + 10), 7)

            # bullet3
            if bullet3Y >= 500:
                bullet_v3 = 0
            else:
                bullet_v3 = 2

            if bullet_v3 == 0:
                bullet3X = playerX + 30
            if bullet_v3 == 2:
                bullet3X = bullet3X
            bullet3Y -= change_bulletY
            if bullet3Y <= -6:
                bullet3Y = 510
                bullet_v3 = 0
            if bullet3Y <= 510 and bullet_v3 == 2:
                pygame.draw.line(screen, (0, 0, 0), (bullet3X, bullet3Y), (bullet3X, bullet3Y + 10), 7)

            # bullet4
            if bullet4Y >= 500:
                bullet_v4 = 0
            else:
                bullet_v4 = 2

            if bullet_v4 == 0:
                bullet4X = playerX + 30
            if bullet_v4 == 2:
                bullet4X = bullet4X
            bullet4Y -= change_bulletY
            if bullet4Y <= -6:
                bullet4Y = 510
                bullet_v4 = 0
            if bullet4Y <= 510 and bullet_v4 == 2:
                pygame.draw.line(screen, (0, 0, 0), (bullet4X, bullet4Y), (bullet4X, bullet4Y + 10), 7)

            # bullet5
            if bullet5Y >= 500:
                bullet_v5 = 0
            else:
                bullet_v5 = 2

            if bullet_v5 == 0:
                bullet5X = playerX + 30
            if bullet_v5 == 2:
                bullet5X = bullet5X
            bullet5Y -= change_bulletY
            if bullet5Y <= -6:
                bullet5Y = 510
                bullet_v5 = 0
            if bullet5Y <= 510 and bullet_v5 == 2:
                pygame.draw.line(screen, (0, 0, 0), (bullet5X, bullet5Y), (bullet5X, bullet5Y + 10), 7)

            # bullet6
            if bullet6Y >= 500:
                bullet_v6 = 0
            else:
                bullet_v6 = 2

            if bullet_v6 == 0:
                bullet6X = playerX + 30
            if bullet_v6 == 2:
                bullet6X = bullet6X
            bullet6Y -= change_bulletY
            if bullet6Y <= -6:
                bullet6Y = 510
                bullet_v6 = 0
            if bullet6Y <= 510 and bullet_v6 == 2:
                pygame.draw.line(screen, (0, 0, 0), (bullet6X, bullet6Y), (bullet6X, bullet6Y + 10), 7)

            # bullet7
            if bullet7Y >= 500:
                bullet_v7 = 0
            else:
                bullet_v7 = 2

            if bullet_v7 == 0:
                bullet7X = playerX + 30
            if bullet_v7 == 2:
                bullet7X = bullet7X
            bullet7Y -= change_bulletY
            if bullet7Y <= -6:
                bullet7Y = 510
                bullet_v7 = 0
            if bullet7Y <= 510 and bullet_v7 == 2:
                pygame.draw.line(screen, (0, 0, 0), (bullet7X, bullet7Y), (bullet7X, bullet7Y + 10), 7)

            # bullet8
            if bullet8Y >= 500:
                bullet_v8 = 0
            else:
                bullet_v8 = 2

            if bullet_v8 == 0:
                bullet8X = playerX + 30
            if bullet_v8 == 2:
                bullet8X = bullet8X
            bullet8Y -= change_bulletY
            if bullet8Y <= -6:
                bullet8Y = 510
                bullet_v8 = 0
            if bullet8Y <= 510 and bullet_v8 == 2:
                pygame.draw.line(screen, (0, 0, 0), (bullet8X, bullet8Y), (bullet8X, bullet8Y + 10), 7)

            # bullet9
            if bullet9Y >= 500:
                bullet_v9 = 0
            else:
                bullet_v9 = 2

            if bullet_v9 == 0:
                bullet9X = playerX + 30
            if bullet_v9 == 2:
                bullet9X = bullet9X
            bullet9Y -= change_bulletY
            if bullet9Y <= -6:
                bullet9Y = 510
                bullet_v9 = 0
            if bullet9Y <= 510 and bullet_v9 == 2:
                pygame.draw.line(screen, (0, 0, 0), (bullet9X, bullet9Y), (bullet9X, bullet9Y + 10), 7)

            # player
            playerX += pX_change
            if playerX <= 1:
                playerX = 1
            if playerX >= 636:
                playerX = 636


            #enemy1
            b_enmy1X = enmy1X + 30
            enmy1Y+=3 #change
            if enmy1Y>=20:
                enmy1Y=20
                enmy1_takeA = 2
                b_enmy1Y+=7 #change
                if b_enmy1Y>=900:
                    b_enmy1Y=30
                b_enmy1XY(enmy1X,enmy1Y)

            enmy1XY(enmy1X,enmy1Y)

            #enmy1destroy
            if enmy1X<=bullet1X<=enmy1X+64 and 20<= bullet1Y <=60 and enmy1_takeA == 2:
                hbullet_v1 = 2
                enmy1_renew = 2
            if enmy1X<=bullet2X<=enmy1X+64 and 20<= bullet2Y <=60 and enmy1_takeA == 2:
                hbullet_v2 = 2
                enmy1_renew = 2
            if enmy1X<=bullet3X<=enmy1X+64 and 20<= bullet3Y <=60 and enmy1_takeA == 2:
                hbullet_v3 = 2
                enmy1_renew = 2
            if enmy1X<=bullet4X<=enmy1X+64 and 20<= bullet4Y <=60 and enmy1_takeA == 2:
                hbullet_v4 = 2
                enmy1_renew = 2
            if enmy1X<=bullet5X<=enmy1X+64 and 20<= bullet5Y <=60 and enmy1_takeA == 2:
                hbullet_v5 = 2
                enmy1_renew = 2
            if enmy1X<=bullet6X<=enmy1X+64 and 20<= bullet6Y <=60 and enmy1_takeA == 2:
                hbullet_v6 = 2
                enmy1_renew = 2
            if enmy1X<=bullet7X<=enmy1X+64 and 20<= bullet7Y <=60 and enmy1_takeA == 2:
                hbullet_v7 = 2
                enmy1_renew = 2
            if enmy1X<=bullet8X<=enmy1X+64 and 20<= bullet8Y <=60 and enmy1_takeA == 2:
                hbullet_v8 = 2
                enmy1_renew = 2
            if enmy1X<=bullet9X<=enmy1X+64 and 20<= bullet9Y <=60 and enmy1_takeA == 2:
                hbullet_v9 = 2
                enmy1_renew = 2

            if enmy1_renew==2 and ( hbullet_v1 == 2 or hbullet_v2==2 or hbullet_v3==2 or hbullet_v4==2 or hbullet_v5==2 or hbullet_v6==2 or hbullet_v7==2 or hbullet_v8==2 or hbullet_v9==2 ) :
                enmy_S= mixer.Sound('assets/sounds/coinS.ogg')
                enmy_S.play()
                enmy1Y=-100
                enmy1X = 50 + random.randrange(0,600,10)
                b_enmy1Y = 30
                enmy1 = random.choice(enemy_images)
                score_value += 1
                enmy1_renew =0
                enmy1_takeA =0
                hbullet_v1 = 0
                hbullet_v2 = 0
                hbullet_v3 = 0
                hbullet_v4 = 0
                hbullet_v5 = 0
                hbullet_v6 = 0
                hbullet_v7 = 0
                hbullet_v8 = 0
                hbullet_v9 = 0

            # enemy2
            b_enmy2X = enmy2X + 30
            enmy2Y += 3  #change
            if enmy2Y >= 20:
                enmy2Y = 20
                enmy2_takeA = 2
                b_enmy2Y += 7 #change
                if b_enmy2Y >= 900:
                    b_enmy2Y = 30
                b_enmy2XY(enmy2X, enmy2Y)

            enmy2XY(enmy2X, enmy2Y)

            # enmy2destroy
            if enmy2X <= bullet1X <= enmy2X + 64 and 20 <= bullet1Y <= 60 and enmy2_takeA == 2:
                hbullet_v1 = 2
                enmy2_renew = 2
            if enmy2X <= bullet2X <= enmy2X + 64 and 20 <= bullet2Y <= 60 and enmy2_takeA == 2:
                hbullet_v2 = 2
                enmy2_renew = 2
            if enmy2X <= bullet3X <= enmy2X + 64 and 20 <= bullet3Y <= 60 and enmy2_takeA == 2:
                hbullet_v3 = 2
                enmy2_renew = 2
            if enmy2X <= bullet4X <= enmy2X + 64 and 20 <= bullet4Y <= 60 and enmy2_takeA == 2:
                hbullet_v4 = 2
                enmy2_renew = 2
            if enmy2X <= bullet5X <= enmy2X + 64 and 20 <= bullet5Y <= 60 and enmy2_takeA == 2:
                hbullet_v5 = 2
                enmy2_renew = 2
            if enmy2X <= bullet6X <= enmy2X + 64 and 20 <= bullet6Y <= 60 and enmy2_takeA == 2:
                hbullet_v6 = 2
                enmy2_renew = 2
            if enmy2X <= bullet7X <= enmy2X + 64 and 20 <= bullet7Y <= 60 and enmy2_takeA == 2:
                hbullet_v7 = 2
                enmy2_renew = 2
            if enmy2X <= bullet8X <= enmy2X + 64 and 20 <= bullet8Y <= 60 and enmy2_takeA == 2:
                hbullet_v8 = 2
                enmy2_renew = 2
            if enmy2X <= bullet9X <= enmy2X + 64 and 20 <= bullet9Y <= 60 and enmy2_takeA == 2:
                hbullet_v9 = 2
                enmy2_renew = 2

            if enmy2_renew == 2 and (
                    hbullet_v1 == 2 or hbullet_v2 == 2 or hbullet_v3 == 2 or hbullet_v4 == 2 or hbullet_v5 == 2 or hbullet_v6 == 2 or hbullet_v7 == 2 or hbullet_v8 == 2 or hbullet_v9 == 2):
                enmy_S = mixer.Sound('assets/sounds/coinS.ogg')
                enmy_S.play()
                enmy2Y = -200
                enmy2X = 600 - random.randrange(0, 500, 5)
                enmy2 = random.choice(enemy_images)
                b_enmy2Y = 30
                score_value+=1
                enmy2_renew = 0
                enmy2_takeA = 0
                hbullet_v1 = 0
                hbullet_v2 = 0
                hbullet_v3 = 0
                hbullet_v4 = 0
                hbullet_v5 = 0
                hbullet_v6 = 0
                hbullet_v7 = 0
                hbullet_v8 = 0
                hbullet_v9 = 0

            # gameoverFalse

        #playerDestry
        if playerX<=b_enmy1X<=playerX+60 and playerY <= b_enmy1Y <= playerY+80 :
            health_value-=25
            b_enmy1Y = 30 #enmy bullet renew
            pattackSo=mixer.Sound('assets/sounds/bomb-alert.ogg')
            pattackSo.play()
        if playerX<=b_enmy2X<=playerX+60 and playerY <= b_enmy2Y <= playerY+80 :
            health_value-=25
            b_enmy2Y = 30 #enmy bullet renew
            pattackSo = mixer.Sound('assets/sounds/bomb-alert.ogg')
            pattackSo.play()

        if health_value <= 0:
            gameOver = True
            mixer.music.stop()
            if gSoundOn == 0:
                gmoverS = mixer.Sound('assets/sounds/govermusic.ogg')
                gmoverS.play(-1)
                gSoundOn=2

        playerXY(playerX, playerY)
        scoreXY(scoreX,scoreY)
        draw_button_pad()
        healthXY(450, 580, health_value)
        if gameOver == False:
            draw_buttons()
        if gameOver == True:
            draw_continue_button()

        if game_start == False:
            screen.blit(cover,(0,0))
            draw_start_button()
        if gameOver == True :
            gameXY(70,300)
        clock.tick(60)  # change
        pygame.display.flip()
        await asyncio.sleep(0)

# This is the program entry point
asyncio.run(main())
