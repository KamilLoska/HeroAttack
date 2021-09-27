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
animation_database['attack'] = load_animation('C:/Users/karni/Documents/GameProject1/attack', [3, 3, 3, 3, 3, 3, 3, 3, 8, 8])
animation_database['idle_enemy'] = load_animation('C:/Users/karni/Documents/GameProject1/idle/idle_enemy', [8, 8, 8, 8, 8, 9, 7, 7, 7, 7])
animation_database['enemy_walk'] = load_animation('C:/Users/karni/Documents/GameProject1/enemy_walk', [8, 8, 8, 8, 8, 9, 7, 7, 7, 7, 7, 7])
animation_database['enemy_attack'] = load_animation('C:/Users/karni/Documents/GameProject1/enemy_attack', [8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 4])
animation_database['secondEnemy_walk'] = load_animation('C:/Users/karni/Documents/GameProject1/secondEnemy_walk', [8, 8, 8, 8, 8, 8])
animation_database['jump'] = load_animation('C:/Users/karni/Documents/GameProject1/jump', [1, 1, 4, 4, 4, 4, 4, 4, 4, 4])

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
    miliseconds_delay2 = 3000
    seconds = 0
    pygame.time.set_timer(second_walk_event, miliseconds_delay2)
    col_spd = 2
    col_dir = [-1, -1, -1]
    def_col = [220, 0, 90]
    global skroll
    skroll = [0, 0]
    divided = [3, 4, 5]

    while loop:
        #print(player_movement[0])
        #for i in range(3):
        #    seconds += + 0.01
            #txt = myfont.render(f"hit: {int(seconds)}", 1, (220, 0, 90))
            #txt = random.random().render(f"hit:" {random.random()})
            #if seconds >= 10:
             #   seconds = 0

        for event in pygame.event.get():
            pygame.time.set_timer(walk_event, miliseconds_delay // 60)
            #pygame.time.set_timer(second_walk_event, miliseconds_delay2 // 60)
            #print(pygame.time.set_timer(second_walk_event, miliseconds_delay2 // 60))
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type ==  walk_event:
                enemy_action, enemy_frame = change_action(enemy_action, enemy_frame, 'enemy_walk')
                if target.x + player_movement[0] > position.x + enemy_movement[0]:
                    enemy_flip = False
                    enemy_movement[0] += 1

                else:
                    enemy_flip = True
                    enemy_movement[0] -= 1

            if event.type == second_walk_event:
                second_enemy_movement[0] -= 2
                second_enemy_action, second_enemy_frame = change_action(second_enemy_action, second_enemy_frame, 'secondEnemy_walk')

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

        keys = pygame.key.get_pressed()
        hitbox = (player_movement[0], player_movement[1] + 619, 40, 60)
        health = 50
        hitboxEnemy = (enemy_movement[0] + 1160, enemy_movement[1] + 625, 40, 60)
        enemy_tuple = pygame.Rect(hitboxEnemy)
        player_tuple = pygame.Rect(hitbox)

        if player_movement[1] > 0:
           player_movement[1] = 0
           if keys[pygame.K_RIGHT]:
                player_action, player_frame = change_action(player_action, player_frame, 'run')
           if keys[pygame.K_LEFT]:
                player_action, player_frame = change_action(player_action, player_frame, 'run')

        if player_movement[0] > 1050 or player_movement[0] < - 10:
            double_side()

        if moving_right :
            player_movement[0] += 2

        if player_rect.x + player_movement[0] == enemy_rect.x - 35 + enemy_movement[0]:
            pygame.time.set_timer(walk_event, miliseconds_delay // 4000)
            enemy_action, enemy_frame = change_action(enemy_action, enemy_frame, 'enemy_attack')

        while True:
            for n in range(8,9):
                if enemy_img_id == f"enemy_attack_{n}":
                    if def_col >[0, 0, 0]:
                        global tenscroll
                        skroll[0] += (player_rect.x  - skroll[0] + 25) / 4
                        skroll[1] += (player_rect.y - skroll[1] - 615) / 330
                        tenscroll = skroll.copy()
                        tenscroll[0] = int(tenscroll[0])
                        tenscroll[1] = int(tenscroll[1])

                            #for i in range():
                        if player_tuple.colliderect(enemy_tuple):

                            draw_text("OUCH!", def_col, player_movement[0] + tenscroll[0], player_movement[1] + 610 + tenscroll[1])
                            if skroll[1] < -58:
                                draw_text("", def_col, player_movement[0], player_movement[1] + 610 )
                                skroll[1] = 0
                            else:
                                def_col = [220, 0, 90]

                    col_change(def_col, col_dir)
            break

        if moving_left:
            player_movement[0] -= 2
        if keys[pygame.K_SPACE]:
            player_action, player_frame = change_action(player_action, player_frame, 'attack')
        if keys[pygame.K_UP]:
                player_action, player_frame = change_action(player_action, player_frame, 'jump')

                if air_timer < 7:
                    vertical_momentum = -6
                if player_movement[1] >= -1:
                    vertical_momentum = -1
                    air_timer = 0
                else:
                    air_timer += 1

        def double_side():
            """From right side to left and conversely"""
            if player_rect[0] + player_movement[0] > 720:
                player_movement[0] = -30
            if player_rect[0] + player_movement[0] < 0:
                player_rect[0] = 1050

        if vertical_momentum >= 3:
            vertical_momentum = 5
        player_movement[1] += vertical_momentum
        vertical_momentum += 0.6

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_RIGHT:
                    moving_right = True
                if event.key == pygame.K_LEFT:
                    moving_left = True

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
               player_movement[0] += player_rect[0]
               player_action, player_frame = change_action(player_action, player_frame, 'idle')
               player_flip = False

            if event.key == pygame.K_LEFT:
                moving_left = False
                player_movement[0] += player_rect[0]
                player_flip = True
                player_action, player_frame = change_action(player_action, player_frame, 'idle')

            if event.key == pygame.K_SPACE:
                player_frame = 6
                player_action, player_frame = change_action(player_action, player_frame, 'idle')

            if event.key == pygame.K_UP:
                player_action, player_frame = change_action(player_action, player_frame, 'jump')


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

        screen.blit(pygame.transform.flip(enemy_img,enemy_flip, False), (enemy_rect[0] + enemy_movement[0], enemy_rect[1] + enemy_movement[1]))
        screen.blit(pygame.transform.flip(second_enemy_img, enemy_flip, False), (second_enemy_rect[0] + second_enemy_movement[0], second_enemy_rect[1] + second_enemy_movement[1]))
        screen.blit(pygame.transform.flip(player_img, player_flip, False), (player_rect[0]  + player_movement[0], player_rect.y  + player_movement[1] + 617))
        pygame.draw.rect(screen, (0, 0, 0), hitbox, 1)
        pygame.draw.rect(screen, (0, 0, 0), hitboxEnemy, 1)
        pygame.draw.rect(screen, (255, 0, 0), (player_movement[0], player_movement[1] + 600, 50, 5))
        pygame.draw.rect(screen, (0, 255, 0), (player_movement[0], player_movement[1] + 600, health, 5))

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()