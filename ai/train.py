import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
"""
Training module for the 2048 game agent.

This script initializes the 2048 game environment, creates an agent,
trains it on the environment, and saves the trained model.
"""
import gym
from agent import Agent
from game_env import Game2048Env

# Register the environment using Gym
gym.envs.registration.register(
    id="2048Env-v0",
    entry_point="game_env:Game2048Env",
)

env = gym.make("2048Env-v0")

agent = Agent(env)
agent.train(timesteps=100000)
agent.save("2048_model")