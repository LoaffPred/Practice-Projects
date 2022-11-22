import pygame

pygame.init()

WIDTH, HEIGHT = 720, 420
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Pygame")


class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.vel = 10

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))


def draw_screen():
    screen.fill(WHITE)
    player.draw(screen)
    pygame.display.update()


player = Player(10, 10, 50, 100, "blue")


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # start here

        draw_screen()

    pygame.quit()


if __name__ == "__main__":
    main()
