"""Custom Environment and Gym interface for the 2048 game."""
import gym
from gym import spaces
from gym.envs.registration import register

import numpy as np


class Game2048Env(gym.Env):
    """Custom Environment that follows gym interface for 2048 game."""

    metadata = {"render.modes": ["console"]}

    def __init__(self):
        """Initialize the environment."""
        super(Game2048Env, self).__init__()
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=0, high=2048, shape=(4, 4), dtype=np.int)
        self.state = np.zeros((4, 4), dtype=np.int)

    def reset(self):
        """Reset the environment to the initial state."""
        self.state = np.zeros((4, 4), dtype=np.int)
        return self.state

    def step(self, action):
        """Execute one timestep within the environment."""
        reward = 0
        done = False
        info = {}
        return self.state, reward, done, info

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
    entry_point="game_env:Game2048Env",
)
