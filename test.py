import pygame
import sys
import time
from card_randomizer import shuffle, shuffle_add, shuffle_remove, count_score
from draw import draw_text

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


# draw text
def draw_text(text, x, y, width, hight, red, green, blue):
    text = font.render(text, True, (red, green, blue))
    text_box = pygame.Rect(x, y, width, hight)
    text_box_center = text.get_rect(center=text_box.center)
    screen.blit(text, text_box_center)


# draw image
def draw_image(file, x, y, scale):
    image = pygame.image.load(file)
    image = pygame.Surface.convert_alpha(image)
    old_x, old_y = image.get_size()
    image = pygame.transform.scale(image, (old_x * scale, old_y * scale))
    screen.blit(image, (x, y))


# Game looop
while running:
    # Loop end
    dt = clock.tick(60)
    print(f"fps: {1000/dt}")

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
    # Loop code

    # Shuffle cards (once)
    if shuffle_deck:
        deck = shuffle(1)
        print(deck[0])
        shuffle_deck = False

    # Display cards
    deck_x = 165
    deck_y = 350
    if deck != []:
        for i in range(0, len(deck)):
            image_card = pygame.image.load("Cards/" + deck[i] + ".png")
            image_card = pygame.Surface.convert_alpha(image_card)
            image_card = pygame.transform.scale(
                image_card, (500 * card_scale, 726 * card_scale)
            )
            screen.blit(image_card, (deck_x + (500 * card_scale + 10) * i, deck_y))

    # Display dealer cards
    ddeck_x = 165
    ddeck_y = 30
    if ddeck != []:
        for i in range(0, len(ddeck)):
            image_card = pygame.image.load("Cards/" + ddeck[i] + ".png")
            image_card = pygame.Surface.convert_alpha(image_card)
            image_card = pygame.transform.scale(
                image_card, (500 * card_scale, 726 * card_scale)
            )
            screen.blit(image_card, (ddeck_x + (500 * card_scale + 10) * i, ddeck_y))

    # hit button
    if hitb_rect.collidepoint(mouse_pos):
        draw_image("Images/wood_button_dark.png", hitb_x, hitb_y, hitb_size)
        draw_text("Hit", hitb_x, hitb_y, hitb_w, hitb_h, 0, 0, 0)
        if mouse_pressed and not hit:
            print("Hit")
            hit = True
            deck = shuffle_add(deck)

    else:
        draw_image("Images/wood_button.png", hitb_x, hitb_y, hitb_size)
        draw_text("Hit", hitb_x, hitb_y, hitb_w, hitb_h, 50, 20, 20)
    # stand button
    if standb_rect.collidepoint(mouse_pos):
        draw_image("Images/wood_button_dark.png", standb_x, standb_y, standb_size)
        draw_text("Stand", standb_x, standb_y, standb_w, standb_h, 0, 0, 0)
        if mouse_pressed and not stand:
            print("Stand")
            deck = shuffle_remove(deck)
            stand = True
    else:
        draw_image("Images/wood_button.png", standb_x, standb_y, standb_size)
        draw_text("Stand", standb_x, standb_y, standb_w, standb_h, 50, 20, 20)
    # player score
    draw_image("Images/wood_board.png", 830, 360, 0.16)
    draw_text(str(round(score)), 830, 360, 169, 169, 51, 20, 9)
    # dealers score
    draw_image("Images/wood_board.png", 830, 30, 0.16)
    draw_text(str(round(dscore)), 830, 30, 169, 169, 51, 20, 9)
    score = count_score(deck)
    dscore = count_score(ddeck)

    draw_image("Images/dealer.png", 2, 20, 0.4)

    pygame.display.flip()

pygame.quit()
