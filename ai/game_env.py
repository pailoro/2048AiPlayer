"""Custom Environment and Gym interface for the 2048 game."""
from atexit import register
import os
import random
import sys

import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "game"))

import gym
from gym import spaces
from gym.envs.registration import regist

import game.logic


class Game2048Env(gym.Env):
    """Custom Environment that follows the gym interface."""

    metadata = {"render.modes": ["human"]}

    def __init__(self):
        """Initializes the 2048 game environment."""
        super(Game2048Env, self).__init__()
        self.action_space = spaces.Discrete(
            4
        )  # 0: cima, 1: baixo, 2: esquerda, 3: direita
        self.observation_space = spaces.Box(
            low=0, high=2048, shape=(4, 4), dtype=np.int
        )
        self.reset()

    def reset(self):
        """Resets the environment and returns it to its initial state."""
        self.state = np.zeros((4, 4), dtype=int)
        self.add_random_tile()
        self.add_random_tile()
        return self.state

    def step(self, action):
        """Performs an action on the environment and returns the resulting state."""
        assert self.action_space.contains(action)
        reward = 0
        done = False
        if action == 0:  # Move up
            self.state = game.logic.move_up(self.state)
        elif action == 1:  # Move down
            self.state = game.logic.move_down(self.state)
        elif action == 2:  # Move left
            self.state = game.logic.move_left(self.state)
        elif action == 3:  # Move right
            self.state = game.logic.move_right(self.state)

        self.add_random_tile()
        if not self.can_move():
            done = True

        return self.state, reward, done, {}

    def add_random_tile(self):
        """Adds a new 2 or 4 block to the grid."""
        empty_cells = [(r, c) for r, c in zip(*np.where(self.state == 0))]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.state[row, col] = 2 if random.random() < 0.9 else 4

    def can_move(self):
        """Checks for remaining valid moves."""
        if np.any(self.state == 0):
            return True
        for i in range(4):
            for j in range(4):
                if i < 3 and self.state[i][j] == self.state[i + 1][j]:
                    return True
                if j < 3 and self.state[i][j] == self.state[i][j + 1]:
                    return True
        return False

    def render(self, mode="console"):
        """Render the current state of the environment."""
        if mode == "console":
            print(self.state)
        else:
            print("Render mode not supported, defaulting to console output.")
            print(self.state)


# Register the environment
register(
    id="2048Env-v0",
    entry_point=__name__ + ":Game2048Env",
)
