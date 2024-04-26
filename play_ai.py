"""
Main module for running the 2048 game automatically using an AI model.

This module sets up the game environment, loads the pre-trained AI model,
and runs the 2048 game autonomously. It relies on the pygame library for
visual rendering and stable_baselines3 for loading and using the PPO model.
"""

import os
import sys
import pygame
import gym

os.environ['SDL_AUDIODRIVER'] = 'dummy'

sys.path.append(os.path.join(os.path.dirname(__file__), 'ai'))

from stable_baselines3 import PPO
from ai.game_env import Game2048Env
from game.constants import SIZE, GRID_LEN, GRID_PADDING, BACKGROUND_COLOR_GAME, BACKGROUND_COLOR_DICT, BACKGROUND_COLOR_CELL_EMPTY, FONT, CELL_COLOR_DICT


# Initialize Pygame
pygame.init()

# Set screen size
screen_size = (SIZE, SIZE)
screen = pygame.display.set_mode(screen_size)

# Set window title
pygame.display.set_caption("2048 AI Player")

# Define colors
color_dict = {
    key: pygame.Color(value) for key, value in BACKGROUND_COLOR_DICT.items()
}
cell_color_dict = {
    key: pygame.Color(value) for key, value in CELL_COLOR_DICT.items()
}
bg_color = pygame.Color(BACKGROUND_COLOR_GAME)

# Define the frame delay (in milliseconds)
frame_delay = 500

def draw_grid(matrix):
    """Draw the game grid and tile numbers on the screen."""
    print(matrix)
    cell_size = SIZE // GRID_LEN
    screen.fill(bg_color)
    for i in range(GRID_LEN):
        for j in range(GRID_LEN):
            cell_value = matrix[i][j]
            cell_rect = pygame.Rect(j * cell_size, i * cell_size, cell_size, cell_size)
            pygame.draw.rect(
                screen,
                color_dict.get(cell_value, bg_color),
                cell_rect.inflate(-GRID_PADDING, -GRID_PADDING)
            )
            if cell_value != 0:
                font = pygame.font.SysFont(*FONT)
                text_surface = font.render(
                    str(cell_value), True, cell_color_dict[cell_value]
                )
                text_rect = text_surface.get_rect(center=cell_rect.center)
                screen.blit(text_surface, text_rect)
    pygame.display.update()

def main():
    """Load the AI model and run the game loop automatically."""
    # Load environment and model
    env = gym.make("2048Env-v0")
    model_path = os.path.join("ai", "2048_model.zip")
    model = PPO.load(model_path)

    # Reset game to initial state
    state = env.reset()
    score = 0

    # Main game loop
    while True:
        # Predict the action from the current state
        action, _states = model.predict(state, deterministic=True)
        print(f"Predicted action: {action}")  # Print the predicted action

        # Execute the action in the environment
        state, reward, done, info = env.step(action)
        
        # Add reward to score and draw the current state
        score += reward
        draw_grid(state)

        # Update the display with the current score
        pygame.display.set_caption(f"2048 AI Player - SCORE: {score}")
        pygame.time.delay(frame_delay)  # Delay to make the game visually trackable

        # Check for game quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Check if the game is over
        if done:
            print(f"Game Over! Final Score: {score}")
            break

if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
