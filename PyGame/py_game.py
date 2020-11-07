# Flappy Bird Pygame version
# Original Code from Clear Code https://youtu.be/UZg49z76cLw
# Modified by Jihyun Nam

import pygame, sys

pygame.init()
pygame.display.set_caption('Flappy Bird')

screen = pygame.display.set_mode((288, 512)) # Create screen object
clock = pygame.time.Clock() # Create clock object

bg_surface = pygame.image.load('sprites/background_day.png') # Load background file
bg_surface = pygame.transform.scale2x(bg_surface) # 2x times scale up

ground_surface = pygame.image.load('sprites/ground.png') # Load background file
ground_surface = pygame.transform.scale2x(ground_surface) # 2x times scale up

ground_xpos = 0

while True:
    # Eveny handler      
    for event in pygame.event.get():    # Getting every single event 
            if event.type == pygame.QUIT:   
                pygame.quit()   # End Game
                sys.exit()  # For safe end program

    # Drawing background 
    screen.blit(bg_surface, (0, 0))

    # Scrolling ground
    ground_xpos -= 0.5    
    screen.blit(ground_surface, (ground_xpos, 450))
    screen.blit(ground_surface, (ground_xpos + 288, 450))
    if(ground_xpos < -288):
        ground_xpos = 0

    # Update display
    pygame.display.update()
    clock.tick(120)
