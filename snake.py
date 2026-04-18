import pygame
import random
import sys

# Init
pygame.init()

# Config
WIDTH, HEIGHT = 720, 480
GRID = 10
SPEED = 15

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

font = pygame.font.SysFont("arial", 20)

# Snake
snake = [[100, 50], [90, 50], [80, 50]]
direction = "RIGHT"

# Fruit
fruit = [
    random.randrange(1, WIDTH // GRID) * GRID,
    random.randrange(1, HEIGHT // GRID) * GRID
]

score = 0


def draw_score():
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))


def game_over():
    screen.fill(BLACK)
    text = font.render(f"Game Over! Score: {score}", True, RED)
    screen.blit(text, (WIDTH // 3, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()


def move_snake(direction, pos):
    x, y = pos
    if direction == "UP":
        y -= GRID
    if direction == "DOWN":
        y += GRID
    if direction == "LEFT":
        x -= GRID
    if direction == "RIGHT":
        x += GRID
    return [x, y]


running = True
while running:
    screen.fill(BLACK)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            if event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            if event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            if event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    # Move snake
    new_head = move_snake(direction, snake[0])
    snake.insert(0, new_head)

    # Eat fruit
    if new_head == fruit:
        score += 10
        fruit = [
            random.randrange(1, WIDTH // GRID) * GRID,
            random.randrange(1, HEIGHT // GRID) * GRID
        ]
    else:
        snake.pop()

    # Draw snake
    for part in snake:
        pygame.draw.rect(screen, GREEN, (*part, GRID, GRID))

    # Draw fruit
    pygame.draw.rect(screen, WHITE, (*fruit, GRID, GRID))

    # Collisions
    if (
        new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT or
        new_head in snake[1:]
    ):
        game_over()

    draw_score()

    pygame.display.update()
    clock.tick(SPEED)

pygame.quit()