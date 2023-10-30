"""
File containing View class
"""
import os
import pygame
from model import Model


class View:
    """
    This class controls the visuals for the game
    """

    def __init__(self, model):
        """
        This method initializes an instance of the View class

        Args:
            self: an instance of the class
            model: an instance of the Model class
        """

        # Set the width and height of the screen
        self.width = 600
        self.height = 400

        # Create a list that will store all of the number images
        self.numbers = []

        self.model = model

        # Get the start screen image
        self.start_screen = pygame.image.load(
            os.path.join("images", "start_screen.PNG")
        ).convert()
        self.start_screen.convert_alpha()

        # Get the main game screen image
        self.main_screen = pygame.image.load(
            os.path.join("images", "main_screen.PNG")
        ).convert()
        self.main_screen.convert_alpha()

        # Get the end screen image
        self.end_screen = pygame.image.load(
            os.path.join("images", "end_screen.PNG")
        ).convert()
        self.end_screen.convert_alpha()

        # Get all the number images
        for i in range(0, 10):
            image = pygame.image.load(
                os.path.join("images", "number" + str(i) + ".png")
            ).convert()
            image.convert_alpha()

            # Make the background transparent
            image.set_colorkey(image.get_at((0, 0)))
            self.numbers.append(image)

        # Set image for ones place to be zero
        self.ones = self.numbers[0]

    def draw_start_screen(self):
        """
        This method creates the start screen
        """
        self.main_screen = pygame.display.set_mode((self.width, self.height))
        self.main_screen.blit(self.start_screen, (0, 0))

    def draw_score(self, score):
        """
        This method takes in the score through model and accordingly
        updates the score on the screen

        Args:
            score: an integer representing the current player score
        """
        string_score = str(score)
        if string_score > 100:
            tens = self.numbers[string_score[0]]
        else:
            tens = self.numbers[string_score[1]]
            hundreds = self.numbers[string_score[0]]
