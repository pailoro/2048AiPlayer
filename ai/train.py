"""
Training module for the 2048 game agent.

This script initializes the 2048 game environment, creates an agent,
trains it on the environment, and saves the trained model.
"""
import os
import sys

from agent import Agent
from game_env import Game2048Env

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "game"))

env = Game2048Env()
agent = Agent(env)
agent.train(timesteps=100000)
agent.save("2048_model.zip")
