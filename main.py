import pygame
from sys import exit

def display_score():
    current_time = (pygame.time.get_ticks() // 100) - start_time
    score_surface = test_font.render(f'Puntaje: {current_time}', False, (64, 64, 64))
    score_rect = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rect)
    return current_time

#Start everything and settings
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0

#Display
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

#score_surface = test_font.render('Score:', False, (64, 64, 64))
#score_rect = score_surface.get_rect(center = (400, 50))


#EnemyNPCs
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (0, 300))

#Player
player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (100 , 300))
player_gravity = 0

#Intro Screen
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

game_name = test_font.render('Hola Nicky Jam!',False, (111, 196, 169))
game_name_rect = game_name.get_rect(center = (400, 80))

game_message = test_font.render('Presiona "Espacio" para empezar, dale!',False, (111, 196, 169))
game_message_rect = game_message.get_rect(center = (400, 320))


#Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #If player presses "X" button, game will close
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:  #if player presses "ESC" button, game will close
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:  #Jumping with Clicks
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300: 
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:    #Jumping with SPACE mechanic
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
                game_active = True
                snail_rect.left = 800
                start_time = (pygame.time.get_ticks() // 100)


    if game_active:
        #blits for background
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))
        #pygame.draw.rect(screen, '#c0e8ec', score_rect)
        #pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        #screen.blit(score_surface, score_rect)
        score = display_score()

        #blits for snail
        screen.blit(snail_surface, snail_rect)
        snail_rect.left -= 4
        if snail_rect.left < -80: snail_rect.left = 800  #respawn the snail after leaving the map
        
        #blits for player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300 : player_rect.bottom = 300
        screen.blit(player_surface, player_rect)

        #collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)

        score_message = test_font.render(f'Tu puntaje: {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center = (400, 320))
        
        game_message_defeat = test_font.render('Perdiste, nerd!',False, (111, 196, 169))
        game_message_defeat_rect = game_message_defeat.get_rect(center = (400, 80))

        game_message_victory = test_font.render('Ganaste Nicky!!!', False, (111, 196, 169))
        game_message_victory_rect = game_message_victory.get_rect(center = (400, 80))
        
        game_message_prize = test_font.render('Tu premio: Te voy a agarrar a palo >:D', False, (111, 196, 169))
        game_message_prize_rect = game_message_prize.get_rect(center = (400, 350))

        if score == 0:
            screen.blit(game_name, game_name_rect)
            screen.blit(game_message, game_message_rect)
        elif score >= 100:
            screen.blit(score_message, score_message_rect)
            screen.blit(game_message_victory, game_message_victory_rect)
            screen.blit(game_message_prize, game_message_prize_rect)
        else:
            screen.blit(score_message, score_message_rect)
            screen.blit(game_message_defeat, game_message_defeat_rect)
        
        


    
    
    pygame.display.update()
    clock.tick(60)