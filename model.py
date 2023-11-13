"""
File containing Model class
"""

import pygame


class Model:
    """
    This is the model class for the game. Since the sprites shown on screen
    are different numbers, it keeps track of the state, and accordingly displays
    the appropriate sprites.

    """

    total_tries = 8

    def __init__(self):
        """
        Initialize an instance of the Model class

        Args:
            score: an integer representing the score of the player
            num_tries: an integer representing how many times the
            player has rolled & scored
            total_tries: an integer representing how many total tries
            the player has

        """
        self.score = 0
        self.num_tries = 0
        self.active = True
        self.tries_left = 8

    def update_score(self, incrementation_val):
        """
        This method updates the score when there is input from the IDE
        """

        self.score += incrementation_val

    def update_tries(self):
        """
        This method updates the number tries the user has left
        """
        self.tries_left = self.total_tries - self.num_tries
