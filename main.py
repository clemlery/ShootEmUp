import pygame
from functools import reduce
from operator import add
from Player import Player

pygame.init()


# CREATING CANVAS
WIDTH : int = 500
HEIGHT : int = 500

PLAYER_WIDTH : int = 20
PLAYER_HEIGHT : int = 20


canvas = pygame.display.set_mode((WIDTH, HEIGHT))

# To make the canvas fullscreen 
# canvas = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

player = Player(WIDTH//2, HEIGHT//2)

# TITLE OF CANVAS
pygame.display.set_caption("My Board")
exit = False

move_map = {pygame.K_UP: ( 0, -1),
            pygame.K_DOWN: ( 0,  1),
            pygame.K_LEFT: (-1,  0),
            pygame.K_RIGHT: ( 1,  0)}

move = []
reduced = (0, 0)

while not exit:
    # LOGIC SECTION
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.KEYDOWN:
            # get all pressed keys
            pressed = pygame.key.get_pressed()
            print(pressed)
            exit = True
            # get all directions the ship should move
            move = [move_map[key] for key in move_map if pressed[key]]

        if move:    
            reduced = reduce(add, move, (0, 0))

    player.moove(reduced)
    # DRAW SECTION
    pygame.display.update()
    canvas.fill((0, 0, 0))
    print(f"player x : {player.x} ; player y : {player.y}")
    pygame.draw.rect(canvas, "white", [player.x, player.y, PLAYER_WIDTH, PLAYER_HEIGHT], 2)