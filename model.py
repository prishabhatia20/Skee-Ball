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
    # scores = [100, 50, 40, 30, 10, 0]
    scores = [100, 50]

    total_tries = 9

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
        self.tries_left = 9

    def update_score(self, sensor_readings):
        """
        This method updates the score when there is input from the IDE
        """

        incrementation_val = 0

        for sensor in sensor_readings:
            if sensor_readings[sensor] == 1:
                incrementation_val += self.scores[sensor]

        self.score += incrementation_val
    def update_tries(self):
        """
        This method updates the number tries the user has left
        """
        self.tries_left -= 1
        self.num_tries += 1
    
    def update_active(self):
        self.active = False
