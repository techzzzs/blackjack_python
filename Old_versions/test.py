import pygame
import sys
import time
from card_randomizer import shuffle, shuffle_add, shuffle_remove, count_score
from draw import draw_text, draw_image

pygame.init()
running = True

# window settings
screen_width = 1000
screen_hight = 600
screen = pygame.display.set_mode((screen_width, screen_hight))
clock = pygame.time.Clock()
pygame.display.set_caption("BlackJack")


image_card = pygame.image.load("Cards/Empty.png")
deck = []
ddeck = ["3_of_h", "back", "back"]
shuffle_deck = False  # start with emty deck
card_scale = 0.25


score = 0
dscore = 0

# text font
font = pygame.font.Font("Images/JMH Typewriter-Black.otf", 30)

# hit button
hitb_x = 6
hitb_y = 350
hitb_size = 0.18
hitb_w = 140
hitb_h = 78
hitb_rect = pygame.Rect(hitb_x, hitb_y, hitb_w, hitb_h)

# stand button
standb_x = 6
standb_y = 450
standb_size = 0.18
standb_w = 140
standb_h = 78
standb_rect = pygame.Rect(standb_x, standb_y, standb_w, standb_h)

gamestate = 1
# gamestate = 0 nozime ending screen
# gamestate = 1 nozime player gajiens
# gamestate = 2 nozime dealera gajiens
# gamestate = 3 nozime betting round

startingHand = []
dealerHand = []

# Game looop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((37, 105, 21))
    # draw_image("Images/background.jpg", 0, 0,0.37)
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()[0]

    # reset pressed buttons
    if not mouse_pressed:
        hit = False
        stand = False

    # hit button
    if hitb_rect.collidepoint(mouse_pos):
        draw_image("Images/wood_button_dark.png", hitb_x, hitb_y, hitb_size)
        draw_text("Hit", hitb_x, hitb_y, hitb_w, hitb_h, 0, 0, 0,30)
        if mouse_pressed and not hit:
            print("Hit")
            hit = True
    else:
        draw_image("Images/wood_button.png", hitb_x, hitb_y, hitb_size)
        draw_text("Hit", hitb_x, hitb_y, hitb_w, hitb_h, 50, 20, 20,30)

    # stand button
    if standb_rect.collidepoint(mouse_pos):
        draw_image("Images/wood_button_dark.png", standb_x, standb_y, standb_size)
        draw_text("Stand", standb_x, standb_y, standb_w, standb_h, 0, 0, 0,30)
        if mouse_pressed and not stand:
            print("Stand")
            stand = True
    else:
        draw_image("Images/wood_button.png", standb_x, standb_y, standb_size)
        draw_text("Stand", standb_x, standb_y, standb_w, standb_h, 50, 20, 20,30)

    # player gajiens
    

    # Display cards
    deck_x = 165
    deck_y = 350
    if deck != []:
        for i in range(0, len(deck)):
            draw_image(
                "Cards/" + deck[i] + ".png",
                deck_x + (500 * card_scale + 10) * i,
                deck_y,
                card_scale,
            )

    # Display dealer cards
    ddeck_x = 165
    ddeck_y = 30
    if ddeck != []:
        for i in range(0, len(ddeck)):
            draw_image(
                "Cards/" + ddeck[i] + ".png",
                ddeck_x + (500 * card_scale + 10) * i,
                ddeck_y,
                card_scale,
            )

    # hit button
    if hitb_rect.collidepoint(mouse_pos):
        draw_image("Images/wood_button_dark.png", hitb_x, hitb_y, hitb_size)
        draw_text("Hit", hitb_x, hitb_y, hitb_w, hitb_h, 0, 0, 0,30)
        if mouse_pressed and not hit:
            print("Hit")
            hit = True
            deck = shuffle_add(deck)
    else:
        draw_image("Images/wood_button.png", hitb_x, hitb_y, hitb_size)
        draw_text("Hit", hitb_x, hitb_y, hitb_w, hitb_h, 50, 20, 20,30)
    # stand button
    if standb_rect.collidepoint(mouse_pos):
        draw_image("Images/wood_button_dark.png", standb_x, standb_y, standb_size)
        draw_text("Stand", standb_x, standb_y, standb_w, standb_h, 0, 0, 0,30)
        if mouse_pressed and not stand:
            print("Stand")
            deck = shuffle_remove(deck)
            stand = True
    else:
        draw_image("Images/wood_button.png", standb_x, standb_y, standb_size)
        draw_text("Stand", standb_x, standb_y, standb_w, standb_h, 50, 20, 20,30)
    # player score
    draw_image("Images/wood_board.png", 830, 360, 0.16)
    draw_text(str(round(score)), 830, 360, 169, 169, 51, 20, 9,30)
    # dealers score
    draw_image("Images/wood_board.png", 830, 30, 0.16)
    draw_text(str(round(dscore)), 830, 30, 169, 169, 51, 20, 9,30)
    score = count_score(deck)
    dscore = count_score(ddeck)

    draw_image("Images/dealer.png", 2, 20, 0.4)

    pygame.display.flip()

pygame.quit()
