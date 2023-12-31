"""
File containing View class
"""
import os
import pygame
# from model import Model


class View:
    """
    This class controls the visuals for the game
    """

    # Set the width and height of the display window

    frame_width = 1370
    frame_height = 1250

    # (0, 0) is in the top left corner of the window
    mid_height = 250
    mid_width = 550


    # Create a display window using Pygame
    world = pygame.display.set_mode([frame_width, frame_height])

    # Load the main screen image
    main_screen = pygame.image.load(
        os.path.join("images", "main_screen.PNG")
    ).convert()


    # Load a copy of main screen in order to be able to refresh the screen
    original_main_screen = pygame.image.load(
        os.path.join("images", "main_screen.PNG")
    ).convert()



    # Load the final score screen image
    score_screen = pygame.image.load(
        os.path.join("images", "score_screen.PNG")
    ).convert()

    # Load the final score screen image
    original_score_screen = pygame.image.load(
        os.path.join("images", "score_screen.PNG")
    ).convert()


    def __init__(self, model):
        """
        This method initializes an instance of the View class

        Args:
            self: an instance of the class
            model: an instance of the Model class
        """
        
        ### IMAGE STORING/LOADING CODE ###

        # Create a list that will store all of the number images
        self.small_numbers = []
        self.big_numbers = []

        # Create a list that stores the start screen images
        self.start_screen = []

        # Load all the start screen images
        for i in range(1, 5):
            image = pygame.image.load(
                os.path.join("images", "start_" + str(i) + ".PNG")
            ).convert()
            self.start_screen.append(image)

        # Load all the small number images
        for i in range(0, 10):
            image = pygame.image.load(
                os.path.join("images", "small_" + str(i) + ".png")
            ).convert()
            image.convert_alpha()

            # Make the background transparent
            image.set_colorkey((255, 255, 255))
            self.small_numbers.append(image)
        
        # Load all the big number images
        for i in range(0, 10):
            image = pygame.image.load(
                os.path.join("images", "big_" + str(i) + ".PNG")
            ).convert()
            image.convert_alpha()

            # Make the background transparent
            image.set_colorkey((255, 255, 255))
            self.big_numbers.append(image)

        # Set image for ones place to be zero
        self.big_zero = self.big_numbers[0]

        # Initialize model

        self.model = model

    def draw_start_screen(self):
        """
        This method creates the start screen
        """

        # Iterate through all start screen images
        for i in range(0, 4):
            # Blit the ith image
            image = i % 4
            self.world.blit(self.start_screen[image], (0, 0))
            # Update display
            pygame.display.flip()
            # Delay the program by one second
            pygame.time.delay(500)
        self.world.blit(self.score_screen, (0, 0))
        pygame.display.flip()

    def draw_main_screen(self):
        """
        This method draws the score screen onto the pygame window
        """
        self.world.blit(self.main_screen, (0, 0))
        pygame.display.flip()
    
    def draw_score_screen(self):
        """
        This method draws the background for the final score screen
        """
        self.world.blit(self.score_screen, (0, 0))
        pygame.display.flip()

    def draw_final_score(self):
        """
        This method parses the last score and blits it onto score_screen
        """

        # Blit the original score screen image on so that the numbers are not stacking
        # on top of each other 
        self.score_screen.blit(self.original_score_screen, (0, 0))

        string_score = str(self.model.score)

        # If the score is greater or equal to 100
        if self.model.score >= 100:
            hundreds = self.big_numbers[int(string_score[0])]
            tens = self.big_numbers[int(string_score[1])]

            self.score_screen.blit(hundreds, ((self.mid_width - 300), self.mid_height))
            self.score_screen.blit(tens, (self.mid_width, self.mid_height))
            self.score_screen.blit(self.big_zero, ((self.mid_width + 300), self.mid_height))

            pygame.display.update()

        ## If the score is less than 100 but greater than 10
        elif self.model.score < 100 and self.model.score >= 10:
            tens = self.big_numbers[int(string_score[0])]

            self.score_screen.blit(tens, ((self.mid_width - 150), self.mid_height))
            self.score_screen.blit(self.big_zero, ((self.mid_width + 150), self.mid_height))

            pygame.display.update()

        # Else, blit 0 in the middle
        else:
            self.score_screen.blit(self.big_zero, (self.mid_width, self.mid_height))
            pygame.display.update()



    def draw_updated_score(self):
        """
        This method takes in the score through model and accordingly
        updates the score on the screen
        """

        # Blit the original main screen image on so that the numbers are not stacking
        # on top of each other 
        self.main_screen.blit(self.original_main_screen, (0, 0))

        string_score = str(self.model.score)

        # If the score is greater or equal to 100
        if self.model.score >= 100:
            hundreds = self.big_numbers[int(string_score[0])]
            tens = self.big_numbers[int(string_score[1])]

            self.main_screen.blit(hundreds, ((self.mid_width - 300), self.mid_height))
            self.main_screen.blit(tens, (self.mid_width, self.mid_height))
            self.main_screen.blit(self.big_zero, ((self.mid_width + 300), self.mid_height))

            pygame.display.update()

        ## If the score is less than 100 but greater than 10
        elif self.model.score < 100 and self.model.score >= 10:
            tens = self.big_numbers[int(string_score[0])]

            self.main_screen.blit(tens, ((self.mid_width - 150), self.mid_height))
            self.main_screen.blit(self.big_zero, ((self.mid_width + 150), self.mid_height))

            pygame.display.update()

        # Else, blit 0 in the middle
        else:
            self.main_screen.blit(self.big_zero, (self.mid_width, self.mid_height))
            pygame.display.update()
        
    def draw_tries(self):
        """
        This method draws the tries the user has left
        """
        self.main_screen.blit(self.small_numbers[self.model.tries_left], (1280, 20))
 