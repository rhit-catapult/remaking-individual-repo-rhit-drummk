import pygame
import sys


def main():
    # pre-define RGB colors for Pygame
    black = pygame.Color("Black")
    white = pygame.Color("White")
    image_size = 470
    TEXT_HEIGHT = 30

    # initialize the pygame module
    pygame.init()

    # prepare the window (screen)
    screen = pygame.display.set_mode((image_size, image_size + TEXT_HEIGHT))
    pygame.display.set_caption("Text, Sound, and an Image")

    # Prepare the image
    # TODO 1: Create an image with the 2dogs.JPG image
    image1 = pygame.image.load("2dogs.JPG")
    # TODO 3: Scale the image to be the size (IMAGE_SIZE, IMAGE_SIZE)
    image1 = pygame.transform.scale(image1, (image_size, image_size + TEXT_HEIGHT))

    # Prepare the text caption(s)
    # TODO 4: Create a font object with a size 28 font.
    font1 = pygame.font.SysFont("arial", TEXT_HEIGHT)
    # TODO 5: Render the text "Two Dogs" using the font object (it's like MAKING an image).
    caption1 = font1.render("Two Dogs", True, white)
    # Prepare the music
    # TODO 8: Create a Sound object from the "bark.wav" file.
    bark = pygame.mixer.Sound("bark.wav")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # TODO 9: Play the music (bark) if there's a mouse click.
            if event.type == pygame.MOUSEBUTTONDOWN:
                bark.play()

        # Clear the screen and set the screen background
        screen.fill(white)

        # Draw the image onto the screen
        # TODO 2: Draw (blit) the image onto the screen at position (0, 0)
        screen.blit(image1, (0, 0))

        # Draw the text onto the screen
        # TODO 6: Draw (blit) the text image onto the screen in the middle bottom.
        # Hint: Commands like these might be useful..
        #          screen.get_width(), caption1.get_width(), image1.get_height()
        screen.blit(caption1, (image1.get_width()//2 - caption1.get_width()//2 - 20,
                               image1.get_height() - 80))

        # TODO 7: On your own, create a new bigger font and in white text place a 'funny' message on top of the image.
        caption2 = font1.render("MEOW", True, black)
        screen.blit(caption2, (image1.get_width() // 2 - caption1.get_width() // 2 + 80,
                               image1.get_height() - 400))

        # Update the screen
        pygame.display.update()


main()
