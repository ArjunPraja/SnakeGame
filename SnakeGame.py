import pygame
import random

# Initialize Pygame
pygame.init()

# Set the width and height of the game window
width, height = 640, 480
window = pygame.display.set_mode((width, height))

# Set the title of the game window
pygame.display.set_caption("Snake Game")

# Define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Set the game clock
clock = pygame.time.Clock()

# Set the initial position and direction of the snake
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = "RIGHT"

# Set the initial position of the food
food_position = [random.randrange(1, (width // 10)) * 10,
                 random.randrange(1, (height // 10)) * 10]
food_spawn = True

# Set the initial score
score = 0

# Function to display the score on the screen
def show_score(choice=1):
    font = pygame.font.SysFont("monospace", 24)
    score_text = font.render("Score: " + str(score), True, white)
    window.blit(score_text, (10, 10))

# Main game loop
game_over = False
while not game_over:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake_direction = "RIGHT"
            elif event.key == pygame.K_LEFT:
                snake_direction = "LEFT"
            elif event.key == pygame.K_UP:
                snake_direction = "UP"
            elif event.key == pygame.K_DOWN:
                snake_direction = "DOWN"

    # Update the snake position based on the direction
    if snake_direction == "RIGHT":
        snake_position[0] += 10
    elif snake_direction == "LEFT":
        snake_position[0] -= 10
    elif snake_direction == "UP":
        snake_position[1] -= 10
    elif snake_direction == "DOWN":
        snake_position[1] += 10

    # Update the snake body
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # Respawn the food
    if not food_spawn:
        food_position = [random.randrange(1, (width // 10)) * 10,
                         random.randrange(1, (height // 10)) * 10]
        food_spawn = True

    # Fill the window with a black color
    window.fill(black)

    # Draw the snake
    for pos in snake_body:
        pygame.draw.rect(window, green, pygame.Rect(
            pos[0], pos[1], 10, 10))

    # Draw the food
    pygame.draw.rect(window, white, pygame.Rect(
        food_position[0], food_position[1], 10, 10))

    # Game over conditions
    if snake_position[0] < 0 or snake_position[0] >= width:
        game_over = True
    if snake_position[1] < 0 or snake_position[1] >= height:
        game_over = True
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over = True

    # Display the score
    show_score()

    # Update the game display
    pygame.display.update()

    # Set the game speed (FPS)
    clock.tick(15)

# Quit the game
pygame.quit()
