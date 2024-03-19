import sys

import pygame

import constants as c
import logic

# Initialize Pygame
pygame.init()

# Set screen size
screen_size = (c.SIZE, c.SIZE)
screen = pygame.display.set_mode(screen_size)

# Set window title
pygame.display.set_caption("2048 AI Player")

# Define colors
color_dict = {
    key: pygame.Color(value) for key, value in c.BACKGROUND_COLOR_DICT.items()
}
cell_color_dict = {key: pygame.Color(value) for key, value in c.CELL_COLOR_DICT.items()}
bg_color = pygame.Color(c.BACKGROUND_COLOR_GAME)


def draw_grid(matrix):
    """
    Draw the game grid and numbers on the screen.
    """
    cell_size = c.SIZE // c.GRID_LEN
    screen.fill(bg_color)
    for i in range(c.GRID_LEN):
        for j in range(c.GRID_LEN):
            cell_value = matrix[i][j]
            cell_rect = pygame.Rect(j * cell_size, i * cell_size, cell_size, cell_size)
            pygame.draw.rect(
                screen,
                color_dict.get(cell_value, bg_color),
                cell_rect.inflate(-c.GRID_PADDING, -c.GRID_PADDING),
            )
            if cell_value != 0:
                font = pygame.font.SysFont(c.FONT[0], c.FONT[1])
                text_surface = font.render(
                    str(cell_value), True, cell_color_dict[cell_value]
                )
                text_rect = text_surface.get_rect(center=cell_rect.center)
                screen.blit(text_surface, text_rect)
    pygame.display.update()


def main():
    matrix = logic.new_game(c.GRID_LEN)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                moved = False
                if event.key in (pygame.K_UP, pygame.K_w, pygame.K_i):
                    matrix, moved = logic.move_up(matrix)
                elif event.key in (pygame.K_DOWN, pygame.K_s, pygame.K_k):
                    matrix, moved = logic.move_down(matrix)
                elif event.key in (pygame.K_LEFT, pygame.K_a, pygame.K_j):
                    matrix, moved = logic.move_left(matrix)
                elif event.key in (pygame.K_RIGHT, pygame.K_d, pygame.K_l):
                    matrix, moved = logic.move_right(matrix)

                if moved:
                    logic.add_two(
                        matrix
                    )  # Update the matrix with a new random '2' after a successful move
                    draw_grid(matrix)  # Redraw the grid with the updated matrix

        draw_grid(matrix)  # Ensure the grid is drawn even if no keys are pressed


if __name__ == "__main__":
    main()
