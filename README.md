# 2048 AI Player

This is a work in progress project aimed at developing an AI player for the popular 2048 game. Currently, the game part is ready and can be played by running the command in the terminal `pytrhon3 game/play.py`.

It is developed using Python3 and the [Pygame](https://pypi.org/project/pygame/) library for the game interface. The AI player is developed using the [Gynasium](https://github.com/Farama-Foundation/Gymnasium) and [Numpy](https://numpy.org/) libraries.

## Installation

To install the necessary dependencies, use the following command:

```bash
pip install -r requirements.txt
```

## Training the Model

The model training is ready and can be initiated by running the following command:

```bash
python3 ai/train.py
```

In the `ai/train.py` file, you can adjust the timesteps parameter in the `agent.train(timesteps=100000)` function to define the number of training iterations for the model.

## Future Work

- TODO: Implement showing the interface playing from the trained model.

- TODO: Create a Dockerfile to set up the entire environment needed to run the project locally.

- TODO: Add animations to the game interface.
