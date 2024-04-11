"""
Module for defining the Agent class using the Stable Baselines3 library.

This module creates an agent that can be trained using the 
Proximal Policy Optimization (PPO) algorithm,
capable of interacting with any given gym environment.
"""

from stable_baselines3 import PPO


class Agent:
    """Define an agent that uses the PPO algorithm for the 2048 game."""

    def __init__(self, env):
        """Initialize the agent with a gym environment."""
        self.model = PPO("MlpPolicy", env, verbose=1)

    def train(self, timesteps=25000):
        """Train the agent for a specified number of timesteps."""
        self.model.learn(total_timesteps=timesteps)

    def save(self, path):
        """Save the trained model to a file."""
        self.model.save(path)
