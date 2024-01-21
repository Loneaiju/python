import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Snake initial position and size
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = 'RIGHT'
change_to = snake_direction
speed = 15

# Food initial position
food_pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
food_spawn = True

# Game over flag
game_over = False

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Change snake direction
    if change_to == 'UP' and not snake_direction == 'DOWN':
        snake_direction = 'UP'
    if change_to == 'DOWN' and not snake_direction == 'UP':
        snake_direction = 'DOWN'
    if change_to == 'LEFT' and not snake_direction == 'RIGHT':
        snake_direction = 'LEFT'
    if change_to == 'RIGHT' and not snake_direction == 'LEFT':
        snake_direction = 'RIGHT'

    # Move the snake
    if snake_direction == 'UP':
        snake_pos[1] -= 10
    if snake_direction == 'DOWN':
        snake_pos[1] += 10
    if snake_direction == 'LEFT':
        snake_pos[0] -= 10
    if snake_direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    # if food and snake collide then scores incremented by 1
    # and new food generated
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        # Increase score
        speed += 1
        food_spawn = False
    else:
        snake_body.pop()
         
    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH//10)) * 10,
                     random.randrange(1, (HEIGHT//10)) * 10]
          
    food_spawn = True
    screen.fill(BLACK)
    
    # Draw snake
    for pos in snake_body:
        pygame.draw.rect(screen, WHITE, pygame.Rect(pos[0], pos[1], 10, 10))
    
    # Draw food
    pygame.draw.rect(screen, GREEN, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    
    # Game Over conditions
    if snake_pos[0] < 0 or snake_pos[0] > WIDTH-10:
        game_over = True
    if snake_pos[1] < 0 or snake_pos[1] > HEIGHT-10:
        game_over = True

    # Check if the snake collides with itself
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over = True
    
    pygame.display.flip()
    
    pygame.time.Clock().tick(speed)

# Quit the game
pygame.quit()
sys.exit()
