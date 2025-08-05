import pygame 
import sys
import random

pygame.init()
# Screen
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Jumping Ball")

# Colors and setup
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

# Ball properties
x = random.randint(20, 580)
y = random.randint(20, 380)
ball_radius = 20
ball_speed_x = 4
ball_speed_y = -4
# y_velocity = -10  # Initial upward velocity
# gravity = 0.5     # Simulates gravity


# Rectangle properties
rect_width = 40
rect_height = 8
rect_x = random.randint(0, 550)
rect_y = 360  # Positioned at the bottom of the screen
speed_rect = 8

clock = pygame.time.Clock() 

# Game loop
running = True 
while running:
    screen.fill(white)

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and rect_x > 0:
        rect_x -= speed_rect
    if keys[pygame.K_RIGHT] and rect_x + rect_width < WIDTH:
        rect_x += speed_rect 


    #movement of the ball
    x += ball_speed_x
    y += ball_speed_y

    # Bounce from left wall
    if x - ball_radius <= 0:
        x = ball_radius
        ball_speed_x *= -1

    # Bounce from right wall
    if x + ball_radius >= WIDTH:
        x = WIDTH - ball_radius
        ball_speed_x *= -1

    # Bounce from top wall
    if y - ball_radius <= 0:
        y = ball_radius
        ball_speed_y *= -1

    # ✅ Paddle collision detection
    if (
        rect_y <= y + ball_radius <= rect_y + rect_height and
        rect_x <= x <= rect_x + rect_width and
        ball_speed_y > 0  ):
        
        y = rect_y - ball_radius
        ball_speed_y *= -1

    pygame.draw.rect(screen, blue, (rect_x, rect_y, rect_width, rect_height))
    pygame.draw.circle(screen, red, (x, y), ball_radius)

    pygame.display.flip()
    clock.tick(60)


pygame.quit()
sys.exit()

            


