TITLE = "MY FLAPPY BIRD"

WIDTH = 400
HEIGHT = 708

background1 = Actor('background', (200, 354))
background2 = Actor('background', (200 + 400, 354))

def draw():
    background1.draw()
    background2.draw()

def update():
    #screen.clear()
    #background1.left = background1.left - 1
    background1.left -= 1
    if background1.left < -400:
        background1.left = 400

    background2.left -= 1
    if background2.left < -400:
        background2.left = 400