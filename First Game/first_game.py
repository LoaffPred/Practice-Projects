import pygame

pygame.init()
pygame.display.set_caption("First Pygame")

WIDTH, HEIGHT = 1000, 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))

def 

def main(window):
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)
