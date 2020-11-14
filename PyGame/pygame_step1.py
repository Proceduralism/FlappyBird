# Flappy Bird Pygame version
# Original Code from Clear Code https://youtu.be/UZg49z76cLw
# Modified by Jihyun Nam

import pygame, sys

pygame.init()

pygame.display.set_caption('Flappy Bird')
screen = pygame.display.set_mode((400, 708)) # Create screen object


while True:
    # Eveny handler      
    for event in pygame.event.get():    # Getting every single event 
            if event.type == pygame.QUIT:                   
                pygame.quit()   # End Game
                sys.exit()  # For safe end program

    pygame.display.update()