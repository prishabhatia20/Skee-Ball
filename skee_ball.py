"""
Main file to run skee ball display
"""

import pygame
from model import Model
from view import View
from parse_messages import parse_message


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

    while model.num_tries < 9:
        ## Parse score
        message = parse_message("/dev/ttyACM0", 9600, model)
        ## Draw main game screen
        ## Function to sense new inputs?
        ## Update score
        ## 




if __name__ == "__main__":
    main()
