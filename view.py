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

    # Set the width and height of the display window

    frame_width = 600
    frame_height = 400

    # Create a display window using Pygame
    world = pygame.display.set_mode([frame_width, frame_height])

    # Load game background image
    background = pygame.image.load(os.path.join("images", "background.PNG")).convert()

    # Get width and height of background image
    bg_width, bg_height = background.get_size()

    def __init__(self, model):
        """
        This method initializes an instance of the View class

        Args:
            self: an instance of the class
            model: an instance of the Model class
        """

        ### IMAGE STORING/LOADING CODE ###

        # Create a list that will store all of the number images
        self.numbers = []
        self.start_screen = []

        # Load all the start screen images
        for i in range(1, 5):
            image = pygame.image.load(
                os.path.join("images", "start" + str(i) + ".png")
            ).convert()
            self.start_screen.append(image)

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

        # Initialize model

        self.model = model

    def draw_start_screen(self):
        """
        This method creates the start screen
        """

        # Iterate through all start screen images
        for i in enumerate(self.start_screen):
            # Blit the ith image
            self.world.blit(self.start_screen[i], (0, 0))
            # Update display
            pygame.display.flip()
            # Delay the program by one second
            pygame.time.delay(1000)

    def draw_score(self):
        """
        This method takes in the score through model and accordingly
        updates the score on the screen

        Args:
            score: an integer representing the current player score
        """
        string_score = str(self.model.score)

        # If the score is less than 100, blit the tens and ones place in a certain
        # position
        if string_score > 100:
            tens = self.numbers[string_score[0]]
            self.world.blit(tens, (200, 300))
            self.world.blit(self.ones, (400, 300))

        ## If the score is greater than 100, blit the hundreds, tens, and ones
        elif string_score <= 100:
            tens = self.numbers[string_score[1]]
            hundreds = self.numbers[string_score[0]]
            self.world.blit(hundreds, (100, 300))
            self.world.blit(tens, (200, 300))
            self.world.blit(self.ones, (300, 300))

        # Else, blit 0 in the middle
        else:
            self.world.blit(self.ones(300, 300))
