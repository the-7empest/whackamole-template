import pygame
import random
GRID_WIDTH, GRID_HEIGHT = 20, 16
SQUARE_SIZE = 32
WINDOW_WIDTH, WINDOW_HEIGHT = GRID_WIDTH * SQUARE_SIZE, GRID_HEIGHT * SQUARE_SIZE
def draw_grid(screen):
     for x in range(0, WINDOW_WIDTH, SQUARE_SIZE):
        pygame.draw.line(screen, "black", (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, SQUARE_SIZE):
        pygame.draw.line(screen, "black", (0, y), (WINDOW_WIDTH, y))
def random_position():
    grid_x = random.randrange(0, GRID_WIDTH) * SQUARE_SIZE
    grid_y = random.randrange(0, GRID_HEIGHT) * SQUARE_SIZE
    return grid_x, grid_y
def main():
    pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    mole_image = pygame.image.load("mole.png")
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                 elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        mouse_x, mouse_y = event.pos
                        mole_x, mole_y = mole_position
                    if mole_x <= mouse_x < mole_x + SQUARE_SIZE and mole_y <= mouse_y < mole_y + SQUARE_SIZE:
                        mole_position = random_position()
                screen.fill("light green")
                draw_grid(screen)
                screen.blit(mole_image, mole_image.get_rect(topleft=mole_position))
                pygame.display.flip()
                clock.tick(60)
            pygame.quit()


if __name__ == "__main__":
    main()
