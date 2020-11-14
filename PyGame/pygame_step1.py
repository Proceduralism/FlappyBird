# Flappy Bird Pygame version
# Original Code from Clear Code https://youtu.be/UZg49z76cLw
# Modified by Jihyun Nam

import pygame, sys

pygame.init()

pygame.display.set_caption('Flappy Bird')
screen = pygame.display.set_mode((400, 708)) # Create screen object

bg_surface1 = pygame.image.load('images/background.png')
bg_surface2 = pygame.image.load('images/background.png')

bg_pos = 0 # bg origin position

while True:
    # Eveny handler      
    for event in pygame.event.get():    # Getting every single event 
            if event.type == pygame.QUIT:                   
                pygame.quit()   # End Game
                sys.exit()  # For safe end program

    bg_pos -= 1 # move 1 pixel every tick

    screen.blit(bg_surface1, (bg_pos, 0))
    screen.blit(bg_surface2, (bg_pos + 400, 0))

    if(bg_pos < -400):
        bg_pos = 0

    pygame.display.update()

    pygame.time.Clock().tick(120)