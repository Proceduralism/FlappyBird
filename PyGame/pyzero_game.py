# Flappy Bird Pygame Zero version


TITLE = "My Flappy Bird"
WIDTH = 400
HEIGHT = 708



def draw():
    #screen.fill((0, 0, 0))
    background1.draw()
    background2.draw()
   
    #bird.draw()

def update():        
    background1.left -= 1
    if background1.left < -400:
        background1.left = 400

    background2.left -= 1
    if background2.left < -400:
        background2.left = 400

#bird = Actor('bird1', (100, 100))

background1 = Actor('background', (200, 354))
background2 = Actor('background', (200 + 400, 354))

