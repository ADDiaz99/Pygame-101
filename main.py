import pygame
from sys import exit

#Start everything and settings
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

#Display
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

score_surface = test_font.render('Score', False, (64, 64, 64))
score_rect = score_surface.get_rect(center = (400, 50))


#EnemyNPCs
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (0, 300))

#Player
player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (100 , 300))

#Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #if event.type == pygame.MOUSEMOTION:
        #    if player_rect.collidepoint(event.pos): print('mouse collides with player')
    
    #blits for background
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
    screen.blit(score_surface, score_rect)

    #blits for snail
    screen.blit(snail_surface, snail_rect)
    snail_rect.left -= 4
    if snail_rect.left < -80: snail_rect.left = 800  #respawn the snail after leaving the map
    
    #blits for player
    screen.blit(player_surface, player_rect)


    #Rectangle collision
    #if player_rect.colliderect(snail_rect):
    #    print('collision')
    
    #mouse_pos = pygame.mouse.get_pos()
    #if player_rect.collidepoint(mouse_pos):
    #    print(pygame.mouse.get_pressed())
    
    
    pygame.display.update()
    clock.tick(60)