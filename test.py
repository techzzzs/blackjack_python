import pygame
import sys

pygame.init()

# Window setup
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blackjack Buttons")
card = pygame.image.load("card.png")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)
DARK_GREEN = (0, 100, 0)
GRAY = (50, 50, 50)

# Font
font = pygame.font.Font(None, 48)

# Define buttons
hit_button = pygame.Rect(200, 450, 150, 60)
stand_button = pygame.Rect(450, 450, 150, 60)

def draw_button(rect, text, hovered=False):
    color = DARK_GREEN if hovered else GREEN
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, BLACK, rect, 3)
    label = font.render(text, True, WHITE)
    screen.blit(label, label.get_rect(center=rect.center))

isRunning: bool = True
# Game loop
while isRunning:
    mouse_pos = pygame.mouse.get_pos()
    screen.fill(WHITE)

    # Check for hover and clicks
    hit_hover = hit_button.collidepoint(mouse_pos)
    stand_hover = stand_button.collidepoint(mouse_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if hit_button.collidepoint(event.pos):
                print("Hit pressed!")
            if stand_button.collidepoint(event.pos):
                print("Stand pressed!")

    # Draw buttons
    draw_button(hit_button, "Hit", hit_hover)
    draw_button(stand_button, "Stand", stand_hover)

    pygame.display.flip()
if isRunning == False:

    pygame.quit()