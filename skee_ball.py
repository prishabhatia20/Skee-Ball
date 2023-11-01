"""
Main file to run skee ball display
"""

import pygame
from model import Model
from view import View


def main():
    """
    Main function to run code. THis function calls all methods
    necessary to display the images, update the score, and calls
    start and end screen methods
    """

    pygame.init()

    # Create an instance of Model
    model = Model()

    # Create an instance of View
    view = View(model)

    view.draw_start_screen()
