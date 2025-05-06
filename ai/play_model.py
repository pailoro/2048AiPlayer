import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

"""
Script to load the trained 2048 AI model and play the game autonomously.
"""

import time
import game_env
from stable_baselines3 import PPO


def main():
    env = game_env.Game2048Env()
    obs = env.reset()

    model = PPO.load("2048_model")

    done = False
    while not done:
        action, _states = model.predict(obs)
        obs, reward, done, info = env.step(action)
        env.render()
        print(f"Reward: {reward}, Status: {info.get('status')}")
        time.sleep(1)  # Pause for a second to observe moves


if __name__ == "__main__":
    main()