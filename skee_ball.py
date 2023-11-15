"""
Main file to run skee ball display
"""

import pygame
from model import Model
from view import View
from parse_messages import parse_message
from pygame.locals import QUIT


def main():
    """
    Main function to run code. THis function calls all methods
    necessary to display the images, update the score, and calls
    start and end screen methods
    """

    pygame.init()

    for event in pygame.event.get():
        if event.type == QUIT:
            # Quit the game if the user clicks the close button
            pygame.quit()

    # Create an instance of Model
    model = Model()

    # Create an instance of View
    view = View(model)

    view.draw_start_screen()

    while model.num_tries < 9:
        ## Draw main game screen
        view.draw_main_screen()

        ## Parse score
        message = parse_message("/dev/ttyACM0", 9600, model)
        if message > 0:

            # Send to model, update scores & tries
            model.update_score(message)
            model.update_tries()
            view.draw_updated_score()

 
            ## Draw main game screen
            ## Function to sense new inputs?
            ## Update score
            ## 
    
    view.draw_end_screen()



if __name__ == "__main__":
    main()
