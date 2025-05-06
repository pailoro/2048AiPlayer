"""Game logic module for the 2048 game.

This module contains all the necessary functions to manage the game state,
manipulate the game grid, and handle player movements and interactions.
Includes functions to start the game, add new tiles, check game status,
move and merge tiles, and calculate scores.
"""
import random

import game.constants as c


def new_game(n):
    """Start a new game by creating an n x n matrix.

    Filled with zeros and adding two '2's in random positions.
    """
    matrix = [[0] * n for _ in range(n)]
    add_two(matrix)
    add_two(matrix)
    return matrix


def add_two(mat):
    """
    Add a '2' or a '4' to a randomly chosen empty cell in the matrix.

    There's a higher probability of adding a '2'.
    """
    empty_cells = [
        (i, j) for i in range(len(mat)) for j in range(len(mat[i])) if mat[i][j] == 0
    ]
    if empty_cells:
        i, j = random.choice(empty_cells)
        # Randomly choose to add a '2' or a '4', with '2' being more likely
        mat[i][j] = 2 if random.random() < 0.9 else 4


def game_state(mat):
    """Check the game state.

    If the player has won, lost, or if the game is not over.
    """
    if any(2048 in row for row in mat):
        return "win"
    if any(0 in row for row in mat) or any_moves_possible(mat):
        return "not over"
    return "lose"


def any_moves_possible(mat):
    """Check if any moves are possible."""
    for i in range(c.GRID_LEN):
        for j in range(c.GRID_LEN):
            if i < c.GRID_LEN - 1 and mat[i][j] == mat[i + 1][j]:
                return True
            if j < c.GRID_LEN - 1 and mat[i][j] == mat[i][j + 1]:
                return True
    return False


def reverse(mat):
    """Reverse each row of the matrix."""
    return [row[::-1] for row in mat]


def transpose(mat):
    """Transpose the matrix (swap rows with columns)."""
    return [list(row) for row in zip(*mat)]


def compress(mat):
    """Compress the matrix by sliding all numbers to the left."""
    changed = False
    new_mat = [[0] * c.GRID_LEN for _ in range(c.GRID_LEN)]
    for i in range(c.GRID_LEN):
        position = 0
        for j in range(c.GRID_LEN):
            if mat[i][j] != 0:
                new_mat[i][position] = mat[i][j]
                if j != position:
                    changed = True
                position += 1
    return new_mat, changed


def calculate_score(mat):
    """Calculate the total score by summing up the values of all tiles."""
    return sum(sum(row) for row in mat)


def merge(mat):
    """
    Merge tiles with the same value by doubling.

    the value of the left tile and setting the right tile to 0.

    """
    changed = False
    for i in range(c.GRID_LEN):
        for j in range(c.GRID_LEN - 1):
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j + 1] = 0
                changed = True
    return mat, changed


def move(mat, direction):
    """Execute a move in the specified direction."""
    if direction == "up":
        return move_up(mat)
    elif direction == "down":
        return move_down(mat)
    elif direction == "left":
        return move_left(mat)
    elif direction == "right":
        return move_right(mat)


def move_left(mat):
    """Move tiles left."""
    mat, compressed = compress(mat)
    mat, merged = merge(mat)
    if merged:
        mat, _ = compress(mat)
    return mat, compressed or merged


def move_right(mat):
    """Move tiles right."""
    mat = reverse(mat)
    mat, moved = move_left(mat)
    mat = reverse(mat)
    return mat, moved


def move_up(mat):
    """Move tiles up."""
    mat = transpose(mat)
    mat, moved = move_left(mat)
    mat = transpose(mat)
    return mat, moved


def move_down(mat):
    """Move tiles down."""
    mat = transpose(mat)
    mat, moved = move_right(mat)
    mat = transpose(mat)
    return mat, moved