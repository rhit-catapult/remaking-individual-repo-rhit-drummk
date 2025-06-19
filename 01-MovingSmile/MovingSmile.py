import pygame
import sys


def main():
    pygame.init()
    pygame.display.set_caption("Moving Smile")
    screen = pygame.display.set_mode((640, 480))

    eye_x = 0
    eye_y = 0
    mouth_y = 0
    clock = pygame.time.Clock()

    while True:
        # TODO 4: Set the clock speed to 60 fps

        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # TODO 3: Make the eye pupils move with Up, Down, Left, and Right keys
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_LEFT]:
                eye_x = eye_x-15
            if keys_pressed[pygame.K_RIGHT]:
                eye_x = eye_x+15

            if keys_pressed[pygame.K_UP]:
                eye_y = eye_y-15
            if keys_pressed[pygame.K_DOWN]:
                eye_y = eye_y+15

            if keys_pressed[pygame.K_SPACE]:
                mouth_y = mouth_y+10

        screen.fill((255, 255, 255))  # white

        # API --> pygame.draw.circle(screen, color, (x, y), radius, thickness)

        pygame.draw.circle(screen, (255, 255, 0), (320, 240), 210)  # yellow circle
        pygame.draw.circle(screen, (0, 0, 0), (320, 240), 210, 4)  # black outline

        pygame.draw.circle(screen, (225, 225, 225), (240, 160), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (240, 160), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), (242+eye_x, 162+eye_y), 7)  # black pupil

        pygame.draw.circle(screen, (225, 225, 225), (400, 160), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (400, 160), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), (398+eye_x, 162+eye_y), 7)  # black pupil

        # TODO 1: Draw a nose
        # Suggestion: color (80,0,0) location (320,245), radius 10
        # API --> pygame.draw.circle(screen, (r,g,b), (x, y), radius, thickness)
        #pygame.draw.ellipse(screen, (225, 200, 0), (320, 215, 100, 100), 2)

        # TODO 2: Draw a mouth
        # Suggestion: color (0,0,0), x 230, y 320, width 180, height 30
        # API --> pygame.draw.rect(screen, (r,g,b), (x, y, width, height), thickness)
        pygame.draw.ellipse(screen, (225, 27, 0), (220, 400-mouth_y, 200, 50))

        pygame.display.update()


main()
