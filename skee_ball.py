"""
Main file to run skee ball display
"""

import pygame
import sys
from model import Model
from view import View
from parse_messages import parse_message
from pygame.locals import QUIT


def main():
    """
    Main function to run code. This function calls all methods
    necessary to display the images, update the score, and calls
    start and end screen methods
    """

    serial_port = "/dev/ttyACM0"
    baud_rate = 9600
    pygame.init()

    for event in pygame.event.get():
        if event.type == QUIT:
            # Quit the game if the user clicks the close button
            # pygame.quit()
            sys.exit()

    # Create an instance of Model
    model = Model()

    # Create an instance of View
    view = View(model)

    view.draw_start_screen()

    while model.num_tries < 9:
        ## Draw main game screen
        view.draw_main_screen()

        ## Parse score
        message = parse_message(serial_port, baud_rate)
        if message != "00":

            # Send to model, update scores & tries
            model.update_score(message)
            model.update_tries()
            view.draw_updated_score()

    
    view.draw_end_screen()



if __name__ == "__main__":
    main()
