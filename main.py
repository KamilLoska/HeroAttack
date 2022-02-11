import pygame
import sys
import os
from pygame.sprite import Group
from Hero import hero
from pygame.math import Vector2
import time
import random

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

global animation_frames
animation_frames = {}

def load_animation(path, frame_durations):
    global animation_frames
    animation_name = path.split('/')[-1]
    animation_frame_data = []
    n = 0

    for frame in frame_durations:
        animation_frame_id = animation_name + '_' + str(n)
        img_loc = path + '/' + animation_frame_id + '.png'
        animation_image = pygame.image.load(img_loc)
        animation_image.set_colorkey((255, 255, 255))
        animation_frames[animation_frame_id] = animation_image.copy()
        for i in range(frame):
            animation_frame_data.append(animation_frame_id)
        n += 1
    return animation_frame_data

def change_action(action_var, frame, new_value):
    if action_var != new_value:
        action_var = new_value
        frame = 0
    return action_var, frame

animation_database = { }
animation_database['idle'] = load_animation('C:/Users/karni/Documents/GameProject1/idle', [14, 14, 14, 14])
animation_database['run'] = load_animation('C:/Users/karni/Documents/GameProject1/run', [7, 7, 7, 7, 7, 7])
animation_database['attack'] = load_animation('C:/Users/karni/Documents/GameProject1/attack', [1, 1, 1, 1, 1, 1, 1, 1, 5, 5])
animation_database['idle_enemy'] = load_animation('C:/Users/karni/Documents/GameProject1/idle/idle_enemy', [8, 8, 8, 8, 8, 9, 7, 7, 7, 7])
animation_database['enemy_walk'] = load_animation('C:/Users/karni/Documents/GameProject1/enemy_walk', [8, 8, 8, 8, 8, 9, 7, 7, 7, 7, 7, 7])
animation_database['enemy_attack'] = load_animation('C:/Users/karni/Documents/GameProject1/enemy_attack', [8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 4])
animation_database['secondEnemy_walk'] = load_animation('C:/Users/karni/Documents/GameProject1/secondEnemy_walk', [8, 8, 8, 8, 8, 8])
animation_database['jump'] = load_animation('C:/Users/karni/Documents/GameProject1/jump', [1, 1, 4, 4, 4, 4, 4, 4, 4, 4])
animation_database['death'] = load_animation('C:/Users/karni/Documents/GameProject1/death', [20, 20, 20, 20, 20, 20, 20, 20, 20,
                                                                                             20, 20, 20, 20, 20, 20])

def main():
    global event, position, target, draw_text
    pygame.init()
    screen = pygame.display.set_mode((1060, 720))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Hero Shooter")
    loop = True
    player_action = 'idle'
    enemy_action = 'enemy_walk'
    second_enemy_action = 'secondEnemy_walk'
    player_frame = 0
    enemy_frame = 0
    second_enemy_frame = 0
    #heroo = Group()
    #heroo.add(Hero)
    background1 = pygame.image.load(resource_path('background.jpg'))
    true_scroll = [0, 0]
    player_movement = [0, 0]
    player_flip = False
    enemy_flip = True
    moving_right = False
    moving_left = False

    vertical_momentum = 0
    air_timer = 0
    screen_rect = screen.get_rect()
    miliseconds_delay = 2000
    walk_event = pygame.USEREVENT + 1
    pygame.time.set_timer(walk_event, miliseconds_delay)
    enemy_movement = [0, 0]
    second_enemy_movement = [0,0]
    second_walk_event = pygame.USEREVENT + 2

    gameRun = pygame.USEREVENT + 3
    pygame.time.set_timer(gameRun, miliseconds_delay)
    miliseconds_delay2 = 3000
    seconds = 0
    pygame.time.set_timer(second_walk_event, miliseconds_delay2)
    col_spd = 1
    col_dir = [-1, -1, -1]
    def_col = [220, 0, 90]
    global skroll
    skroll = [0, 0]
    divided = [3, 4, 5]
    health = 50
    myfont = pygame.font.SysFont("comicsansms", 15)
    enemy_mov = [0, 0]
    global walking_enemy
    walking_enemy = True
    global mobHealth
    global healths
    global new_move
    global mobs1
    change_frame = 0
    mobHealth = 50
    healths = [50, 50, 50]
    new_move = [0, 0]
    walkings = []
    moving = [0, 0]
    moveMe = []
    global deathFrame
    deathFrame = 0
    poops = []
    for l in range(3):
        walkings.append(walking_enemy)
        moveMe.append(moving.copy())
        poops.append(deathFrame)

    gameRun = False
    while loop:

        for i in range(3):
            seconds += 0.01
            txt = myfont.render(f"hit: {int(seconds)}", 1, (220, 0, 90))
            if seconds >= 10:
                seconds = 0

        for event in pygame.event.get():
            pygame.time.set_timer(walk_event, miliseconds_delay // 80)


            #pygame.time.set_timer(second_walk_event, miliseconds_delay2 // 60)
            #print(pygame.time.set_timer(second_walk_event, miliseconds_delay2 // 60))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            #if event.type == walk_event:
            global rects, RectDict, mobs

            for i, v in enumerate(moveMe):

                #if target.x + player_movement[0] > position.x + moveMe[i][0]:
                enemy_flip = False
                    #enemy_mov[0] += 2
                #if moveMe[i][0] >= 0:
                 #   moveMe[i][0] += 2
                    #for m in range(3):
                        #   if healths[m] <= 0:
                        #      pygame.time.set_timer(walk_event, 0)
                        #     enemy_action, enemy_frame = change_action(enemy_action, enemy_frame, 'death')

                if moveMe[i][0] <= 0:

                    enemy_flip = True
                #if target.x + player_movement[0] < position.x + moveMe[i][0]:
                    # enemy_mov[0] -= 2
                    moveMe[i][0] -= 2
                    #for n in range(3):



                    #for m in range(3):
                     #   if healths[m] <= 0:
                            #pygame.time.set_timer(walk_event, 5000, 1)
                      #         enemy_action, enemy_frame = change_action(enemy_action, enemy_frame, 'death')


            #if event.type == second_walk_event:
             #   second_enemy_movement[0] -= 2
              #  second_enemy_action, second_enemy_frame = change_action(second_enemy_action, second_enemy_frame, 'secondEnemy_walk')

        player_frame += 1
        if player_frame >= len(animation_database[player_action]):
            player_frame = 0

        player_img_id = animation_database[player_action][player_frame]
        player_img = animation_frames[player_img_id]
        player_rect = player_img.get_rect()

        enemy_frame += 1
        if enemy_frame >= len(animation_database[enemy_action]):
            enemy_frame = 0
        enemy_img_id = animation_database[enemy_action][enemy_frame]
        enemy_img = animation_frames[enemy_img_id]
        enemy_rect = enemy_img.get_rect()

        second_enemy_frame += 1
        if second_enemy_frame >= len(animation_database[second_enemy_action]):
            second_enemy_frame = 0

        second_enemy_img_id = animation_database[second_enemy_action][second_enemy_frame]
        second_enemy_img = animation_frames[second_enemy_img_id]
        second_enemy_rect = second_enemy_img.get_rect()
        target = Vector2(player_rect[0], player_rect[1])
        enemy_rect.x = 1160
        enemy_rect.y = 625
        second_enemy_rect.x = 1280
        second_enemy_rect.y = 625
        position = Vector2(enemy_rect[0], enemy_rect[1])

        screen.blit(background1, (0, 0))

        true_scroll[0] += (player_rect.x-true_scroll[0]-10)/10
        true_scroll[1] += (player_rect.y - true_scroll[1] - 615) / 30

        scroll = true_scroll.copy()
        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])


        global tenscroll
        skroll[0] += (player_rect.x - skroll[0] + 25) / 4
        skroll[1] += (player_rect.y - skroll[1] - 410) / 180
        tenscroll = skroll.copy()
        tenscroll[0] = int(tenscroll[0])
        tenscroll[1] = int(tenscroll[1])

        keys = pygame.key.get_pressed()
        hitbox = (player_rect[0] + player_movement[0], player_rect[1] + player_movement[1] - 40, 40, 60)
        hitboxEnemy = (enemy_movement[0] + 1160, enemy_movement[1] + 625, 40, 60)
        enemy_tuple = pygame.Rect(hitboxEnemy)
        player_tuple = pygame.Rect(hitbox)
        if player_movement[1] > 0:
           player_movement[1] = 0

        if player_movement[0] > 1050 or player_movement[0] < - 10:
            double_side()

        if moving_right and keys[pygame.K_RIGHT]:
            player_movement[0] += 2
        elif moving_left and keys[pygame.K_LEFT]:
            player_movement[0] -= 2

        #if player_rect.x + player_movement[0] == enemy_rect.x - 35 + enemy_movement[0]:
         #   pygame.time.set_timer(walk_event, miliseconds_delay // 4000)
          #  enemy_action, enemy_frame = change_action(enemy_action, enemy_frame, 'enemy_attack')

        if def_col > [0, 0, 0]:

            if player_tuple.colliderect(enemy_tuple):
                if enemy_frame == 70:
                    health -= 4
                    draw_text("4", def_col, player_movement[0] + tenscroll[0],
                              player_movement[1] + 640 + tenscroll[1])

                elif enemy_frame >= 74:
                    draw_text("4", def_col, player_movement[0] + tenscroll[0],
                            player_movement[1] + 640 + tenscroll[1])

                else:
                    if skroll[1] < -95:
                        draw_text("", def_col, player_movement[0], player_movement[1] + 660 )
                        skroll[1] = player_rect.x

                    else:
                        def_col = [220, 0, 90]
                        #print(health)
                    col_change(def_col, col_dir)


        #if keys[pygame.K_SPACE]:
         #   player_action, player_frame = change_action(player_action, player_frame, 'attack')

        if keys[pygame.K_UP]:
            player_action, player_frame = change_action(player_action, player_frame, 'jump')


            if air_timer < 7:
                vertical_momentum = -6
            if player_movement[1] >= -1:
                vertical_momentum = -1
                air_timer = 0
            else:
                air_timer += 1

        def hitMob(img, posX, posXmob, posY, posYmob, player_action, frame, flip):
            global mobHealth

            #if player_tuple.colliderect(enemy_tuple):
             #   if player_action == 'attack':
              #      mobHealth -= 0.5
               #     print(mobHealth)

            if mobHealth > 0:

                screen.blit(pygame.transform.flip(img, flip, False),
                            (posX + posXmob, posY + posYmob))

                pygame.draw.rect(screen, (255, 0, 0),
                                 (posXmob + posX, posY + posYmob, 50, 5))

                pygame.draw.rect(screen, (0, 255, 0),
                                 (posXmob + posX, posY + posYmob, mobHealth, 5))

        def double_side():
            """From right side to left and conversely"""
            if player_rect[0] + player_movement[0] > 720:
                player_movement[0] = -30
            if player_rect[0] + player_movement[0] < 0:
                player_rect[0] = 1050

        def spawn_mobs(enemy_action, enemy_frame, animation_database, enemy_flip, moveMe):

            global mobHealth, healths, new_move, rects, RectDict, deathFrame
            mobs = []
            DeleteMobs = []
            dictt = {}
            enemy_img_ID = animation_database[enemy_action][enemy_frame]
            enemy_IMG = animation_frames[enemy_img_ID]
            enemy_rectt = enemy_IMG.get_rect().copy()
            rects = []
            mobs1 = []
            dictTrue = {}
            RectDict = {}
            rect_enemy = enemy_IMG.get_rect().copy()
            divind = 60
            myRect = []


            hitbox = (player_movement[0], player_movement[1] + 619, 40, 60)
            player_tuple = pygame.Rect(hitbox)
            global walking_enemy

            enemy_rectt.x = 1050
            current_posX = enemy_rectt.x + enemy_mov[0]

            for k in range(3):
                enemy_rectt.x += 66
                enemys_rect = (enemy_rectt.copy().x +  moveMe[k][0])
                rects.append(enemys_rect)

            print(poops)
            dictTrue[f'{rects}'] = walkings

            for i in range(3):
                mobs.append(enemy_IMG)

                dictt[mobs[i]] = healths
                #RectDict[rects[i]] = moving[i][0]

                enemy_rectt[1] = 625

                #for index, item in enumerate(rects):
                #for item, value in sorted(enumerate(rects), reverse = True):
                draw = moveMe.copy()

                if healths[i] >= 0:
                    #screen.blit(pygame.transform.flip(mobs[i], enemy_flip, False), ((RectDict[rects[i]]), enemy_rectt[1]))
                        screen.blit(pygame.transform.flip(mobs[i], enemy_flip, False), ((rects[i]), enemy_rectt[1]))

                        pygame.draw.rect(screen, (255, 0, 0),
                                (rects[i], enemy_rectt[1], 50, 5))
                        pygame.draw.rect(screen, (0, 255, 0),
                                (rects[i], enemy_rectt[1], healths[i], 5))


                if healths[i] <= 0:
                    for z in range(len(str(i))):

                            if poops[i] <= 13:
                                poops[i] += 1

                                if i >= 14:
                                    z += 1
                                    i = 0

                            mobs[i] = animation_frames[f'death_{poops[i]}']

                    #else:
                     #   clock.tick(30)
                    #enemy_action, enemy_frame = change_action(enemy_action, enemy_frame, 'death')

                    #moveMe[i][0] = -moveMe[i][0]
                            moveMe[i][0] += 2

                            if moveMe[i][0] %3:
                                moveMe[i][0] -= 2

                            screen.blit(pygame.transform.flip(mobs[i], enemy_flip, False), ((rects[i]), enemy_rectt[1]))

                i = 0
                if player_action == 'attack':
                        #mobHealth -= 0.5

                    for h in healths:
                        healths[i] -= 0.5
                        if h <= 0:
                            i += 1

                            #enemy_action, enemy_frame = change_action(enemy_action, enemy_frame, 'death')
                            #deathFrame = 0


                    for k, v in dictt.items():
                        if v[2] <= 0 and h <= 0:
                            healths = [50, 50, 50]
                            enemy_rectt[0] -= 1180


        if vertical_momentum >= 3:
            vertical_momentum = 5

        player_movement[1] += vertical_momentum
        vertical_momentum += 0.6

        if player_rect[1] + player_movement[1] >= 5 and moving_right == False and moving_left == False:

            player_action, player_frame = change_action(player_action, player_frame, 'idle')
        if keys[pygame.K_SPACE]:
            player_action, player_frame = change_action(player_action, player_frame, 'attack')


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                #if event.key == pygame.K_RIGHT:
                 #   moving_right = True
                #if event.key == pygame.K_LEFT:
                #    moving_left = True

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                 moving_right = True
                 player_action, player_frame = change_action(player_action, player_frame, 'run')

                 player_flip = False

            if event.key == pygame.K_LEFT:
                player_flip = True
                moving_left = True
                player_action, player_frame = change_action(player_action, player_frame, 'run')


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
               moving_right = False
               #player_movement[0] /= 3
               player_movement[0] += player_rect[0]
               player_action, player_frame = change_action(player_action, player_frame, 'idle')
               player_flip = False

            if event.key == pygame.K_LEFT:
                moving_left = False
                player_movement[0] += player_rect[0]
                player_flip = True
                player_action, player_frame = change_action(player_action, player_frame, 'idle')


            #if event.key == pygame.K_SPACE:
                #player_frame = 8
             #   player_action, player_frame = change_action(player_action, player_frame, 'idle')


            if event.key == pygame.K_UP:
                #vertical_momentum = 5

               # print(animation_frames)
                #player_action, player_frame = change_action(player_action, player_frame, 'idle')
                #print(vertical_momentum)
             #   player_action, player_frame = change_action(player_action, player_frame, 'jump')
              #  if player_movement[1] == 5:

            #if player_movement[0] > 0 and keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
             #   player_action, player_frame = change_action(player_action, player_frame, 'run')

                pass
                #player_action, player_frame = change_action(player_action, player_frame, 'idle')

        def draw_text(text, col, x, y):
            font = pygame.font.SysFont("comicsansms", 15)
            text_surface = font.render(text, 1, col)
            text_surface.set_colorkey((255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.center = (x, y)
            screen.blit(text_surface, text_rect)

        def col_change(col, dir):
            for i in range(3):
                col[i] += col_spd * dir[i]
                if col[i] >= 255:
                    col[i] = 0
                elif col[i] <= 0:
                    col[i] = 0
        #print(player_frame == 15)
        #screen.blit(pygame.transform.flip(enemy_img,enemy_flip, False), (enemy_rect[0] + enemy_movement[0], enemy_rect[1] + enemy_movement[1]))
        #screen.blit(pygame.transform.flip(second_enemy_img, enemy_flip, False), (second_enemy_rect[0] + second_enemy_movement[0], second_enemy_rect[1] + second_enemy_movement[1]))
        #pygame.draw.rect(screen, (0, 0, 0), hitbox, 1)
        #pygame.draw.rect(screen, (0, 0, 0), hitboxEnemy, 1)]
        spawn_mobs(enemy_action, enemy_frame, animation_database, enemy_flip, moveMe)


        #hitMob(enemy_img, enemy_rect[0], enemy_movement[0], enemy_rect[1], enemy_movement[1], player_action,
         #      enemy_frame, enemy_flip)

        #screen.blit(txt, (player_movement[0], player_movement[1] + 610))
        if health >= 0:
            screen.blit(pygame.transform.flip(player_img, player_flip, False),
                        (player_rect[0] + player_movement[0], player_rect.y + player_movement[1] + 617))
            pygame.draw.rect(screen, (255, 0, 0), (player_movement[0], player_movement[1] + 600, 50, 5))
            pygame.draw.rect(screen, (0, 255, 0), (player_movement[0], player_movement[1] + 600, health, 5))
            pygame.draw.rect(screen, (255, 255, 33), (0, 680, 1200, 5))

        else:

            player_img = pygame.Surface([0,0])
            screen.blit(player_img, (0,0))
        #else:

            #enemy_img = pygame.Surface([0,0])
            #screen.blit(enemy_img, (0,0))

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()