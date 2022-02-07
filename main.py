import pygame
import classes
import time

#window
pygame.init()
win = pygame.display.set_mode((900,800))

#var
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
width = 50
grid_blocks = []
clock = pygame.time.Clock()
test = classes.TwoByTwoBlock(0, 0, width, red, [], win)
timer = 0

def render():
    #background 
    pygame.draw.rect(win, white, pygame.Rect(0, 0, 900, 800))

    test.draw()
    #grid
    pygame.draw.rect(win, black, pygame.Rect(200, 0, 500, 800), 4)
    for y in range(16):
        for x in range(10):
            grid_blocks.append(classes.GridBlock(x, y, width, width, 3, black, win, False))

    #for grid_block in grid_blocks:
        #grid_block.draw()   

       

         

#main loop
run = True
while run:
    timer += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and test.static() == False:
        test.moveright()

    if keys[pygame.K_LEFT] and test.static() == False:
        test.movelift()
    if test.static() == False and timer % 10 == 0:
        test.movedown()

    #display update
    clock.tick(10)    
    render()
    pygame.display.update()
    pygame.display.flip()        