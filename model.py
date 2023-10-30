"""
File containing Model class
"""

import pygame


class Model:
    """
    This is the model class for the game. Since the sprites shown on screen
    are different numbers, it keeps track of the state, and accordingly displays
    the appropriate sprites.

    Attributes:
        score: an integer representing the score of the player
        num_tries: an integer representing how many times the
        player has rolled & scored
        total_tries: an integer representing how many total tries
        the player has
    """

    score = 0
    num_tries = 0
    total_tries = 8

    def __init__(self, player):
        """
        Initialize an instance of the Model class

        Args:
            player: an instance of the

        """
