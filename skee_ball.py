"""
Main file to run skee ball display
"""

import pygame
import sys
from model import Model
from view import View
from parse_messages import *
from pygame.locals import QUIT


def main():
    """
    Main function to run code. This function calls all methods
    necessary to display the images, update the score, and calls
    start and end screen methods
    """

    serial_port = "/dev/ttyACM0"
    baud_rate = 9600

    try:
        arduino = serial.Serial(serial_port, baud_rate, timeout=0.5)
    except:
        print("Please check the port and baud rate")


    pygame.init()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Quit the game if the user clicks the close button
            pygame.quit()

    # Create an instance of Model
    model = Model()

    # Create an instance of View
    view = View(model)

    view.draw_start_screen()
    
    clock = pygame.time.Clock()

    while model.active:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quit the game if the user clicks the close button
                pygame.quit()
        # Draw main game screen
        view.draw_main_screen()

        if model.num_tries == 0:
            view.draw_updated_score()
            view.draw_tries()

        ## Parse score
        message = parse_message(serial_port, baud_rate, arduino)
        print(f"Message: {message}")
        if "1" in message:

            # Send to model, update scores & tries
            model.update_score(message)
            model.update_tries()
            view.draw_updated_score()
            view.draw_tries()
            model.update_active()

        pygame.display.flip()
        
        # pygame.display.update()
        clock.tick(60)
        

    
    view.draw_end_screen()
    pygame.display.update()



if __name__ == "__main__":
    main()
