import pygame
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

while not exit:
    # LOGIC SECTION
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == pygame.KEYDOWN:
            match event.type:
                case pygame.K_UP:
                    player.moove((0, 1))
                case pygame.K_DOWN:
                    player.moove((0, -1))
                case pygame.K_LEFT:
                    player.moove((-1, 0))
                case pygame.K_RIGHT:
                    player.moove((1, 0))
    print(f"player x : {player.x} ; player y : {player.y}")
    print(player.moove((0, 0)))
    # DRAW SECTION
    pygame.draw.rect(canvas, "white", [player.x, player.x, PLAYER_WIDTH, PLAYER_HEIGHT], 2)
    pygame.display.update()