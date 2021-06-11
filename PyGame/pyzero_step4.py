import pgzrun
import random

TITLE = "FLAPPY BIRD"

WIDTH = 400
HEIGHT = 708

background1 = Actor('background', (200, 354))
background2 = Actor('background', (200 + 400, 354))

bird_dead = Actor('birddead', (0, 0))

gap = 100

top_pipe = Actor('top', (300,0))
bottom_pipe = Actor('bottom', (300, 500 + gap))

bird = Actor('bird0', (75, 500))

bird.speed = 1

bird.score = 0


def draw():
    background1.draw()
    background2.draw()

    top_pipe.draw()
    bottom_pipe.draw()

    bird.draw()


    screen.draw.text('{}: {}'.format("Score", bird.score), (20, 20)) 

  

def update():
    #screen.clear()
    #background1.left = background1.left - 1    

    background1.left -= 1
    if background1.left < -400:
        background1.left = 400

    background2.left -= 1
    if background2.left < -400:
        background2.left = 400

    bird.y += bird.speed

    top_pipe.x -= 1
    if top_pipe.x < -50:
        top_pipe.x = 400

        top_pipe.y = random.random() * 200
       
    bottom_pipe.x -= 1

    if bottom_pipe.x < -50:
        bottom_pipe.x = 400

        bottom_pipe.y = top_pipe.y + 600

    if bird.y > HEIGHT or bird.y < 0:
        reset()

    if (bird.colliderect(top_pipe) or bird.colliderect(bottom_pipe)):
        hit_pipe()
    

    if bird.x > top_pipe.right and bird.x < top_pipe.right + 2:
        bird.score += 10


def on_mouse_down():
    print ('The mouse was clicked')
    #bird.y -= 100
    animate(bird, duration=0.35, pos=(bird.x + 10, bird.y - 50))

def hit_pipe():
    print ("Hit pipe!")
    bird.image = "birddead"
    animate(bird, duration=5, pos=(500, 1000))

def reset():
    print ("Back to the start...")
    bird.speed = 1
    bird.center = (75, 100)
    bird.image = "bird0"
    bird.alive = True
    bird.score = 0
    top_pipe.center = (300, 0)
    bottom_pipe.center = (300, top_pipe.height + gap)    


pgzrun.go()        