import pygame
import sys
from card_randomizer import shuffle

pygame.init()

running = True

screen_width = 900
screen_hight = 600
screen = pygame.display.set_mode((screen_width, screen_hight))
clock = pygame.time.Clock()
pygame.display.set_caption("BlackJack")


image = pygame.image.load("Cards/Empty.png")
deck = []
shuffle_deck = True
card_scale = 0.25


# Game looop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((80, 180, 80))

    # Loop code

    # Shuffle cards
    if shuffle_deck:
        deck = shuffle(3)
        print(deck[0])
        shuffle_deck = False

    # Display cards
    if deck != []:
        for i in range(0, len(deck)):
            image = pygame.image.load("Cards/" + deck[i] + ".png")
            image = pygame.Surface.convert_alpha(image)
            image = pygame.transform.scale(image, (500 * card_scale, 726 * card_scale))
            screen.blit(image, (100 + (500 * card_scale + 10) * i, 100))

    # Loop end
    dt = clock.tick(60) / 1000
    pygame.display.flip()

pygame.quit
