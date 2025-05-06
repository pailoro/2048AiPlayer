"""Custom Environment and Gym interface for the 2048 game."""
import game.logic as logic
from game import constants as c
import gym
import numpy as np
from gym import spaces
from gym.envs.registration import register


class Game2048Env(gym.Env):
    """Custom Environment that follows gym interface for 2048 game."""

    metadata = {"render.modes": ["console"]}

    def __init__(self):
        super(Game2048Env, self).__init__()
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=0, high=2048, shape=(c.GRID_LEN, c.GRID_LEN), dtype=np.int32)
        self.state = None
    def reset(self):
        self.state = logic.new_game(c.GRID_LEN)
        self.score = logic.calculate_score(self.state)
        return np.array(self.state, dtype=np.int32)
    def step(self, action):
        directions = ["up", "down", "left", "right"]
        direction = directions[action]
        prev_state = [row[:] for row in self.state]
        self.state, logic.moved = logic.move(self.state, direction)
        reward = 0
        done = False
        if logic.moved:
            logic.add_two(self.state)
        new_score = logic.calculate_score(self.state)
        reward = new_score - self.score
        self.score = new_score
        status = logic.game_state(self.state)
        if status == "win" or status == "lose":
            done = True
        info = {"status": status}
        return np.array(self.state, dtype=np.int32), reward, done, info
    def render(self, mode="console"):
        """
        Render the current state of the board in a readable grid format.
        """
        if mode == "console":
            board = np.array(self.state)
            for row in board:
                print(" ".join(f"{val:4}" if val != 0 else "   ." for val in row))
        else:
            print("Render mode not supported, defaulting to console output.")
            board = np.array(self.state)
            for row in board:
                print(" ".join(f"{val:4}" if val != 0 else "   ." for val in row))