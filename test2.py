import pygame, os
import math
import time
import sys
from card_randomizer import shuffle, shuffle_add, shuffle_remove, count_score
from draw import draw_text, draw_image, draw_image_c

pygame.init()
running = True


# window settings
info = pygame.display.Info()
# screen_width, screen_height = 1920, 1080
# screen_w, screen_h = 1280, 720
screen_w, screen_h = 1536, 793
screen = pygame.display.set_mode(
    (screen_w, screen_h), pygame.RESIZABLE | pygame.WINDOWMAXIMIZED
)
clock = pygame.time.Clock()
pygame.display.set_caption("BlackJack")


# rectangles
rect_play = pygame.Rect(649, 580, 238, 118)
rect_hit = pygame.Rect(30, 550, 225, 125)
rect_stand = pygame.Rect(30, 700, 225, 125)
rect_allin = pygame.Rect(1250, 390, 135, 44)
rect_allout = pygame.Rect(1395, 390, 135, 44)
rect_half = pygame.Rect(1250, 440, 280, 44)
rect_100plus = pygame.Rect(1250, 490, 135, 44)
rect_100minus = pygame.Rect(1395, 490, 135, 44)
rect_submit = pygame.Rect(618, 360, 300, 100)
rect_playagain = pygame.Rect(468, 600, 600, 100)


# settings
state = 0
states = {
    0: "Main tittle",
    1: "Place your bet (click to submit)",
    2: "Hit or Stand?",
    3: "Dealer's Turn",
    4: "You Won",
    5: "You Lost",
    6: "Draw",
}
# state 0 - main tittle
# state 1 - betting
# state 2 - player gajiens
# state 3 - dealera gajiens
# state 4 - winner
# state 5 - Looser
# state 6 - draw

deck = []  # player deck
ddeck = []  # dealer deck
bet = 0
balance = 10000
pressed = False
score = 0
dscore = 0
timer = 0
card_added = True
dealer_hit = False
dealer_stand = False
player_stand = False
money_delt = False

# game loop
running = True
while running:
    dt = clock.tick(60)
    timer += dt

    if timer >= 1000:
        timer -= 1000
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # actions
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

        # state 0
        if state == 0:
            if rect_play.collidepoint(event.pos):
                state = 1

        # state 1
        if state == 1 and not pressed:
            if rect_allout.collidepoint(event.pos) and bet > 0:
                balance = balance + bet
                bet = 0
            if balance > 0:
                if rect_allin.collidepoint(event.pos):
                    bet = bet + balance
                    balance = 0
                if rect_half.collidepoint(event.pos):
                    difference = round(balance / 2)
                    bet = bet + difference
                    balance = balance - difference

                # +100 or -100 buttons
                if balance >= 100:
                    if rect_100plus.collidepoint(event.pos):
                        bet = bet + 100
                        balance = balance - 100
            if bet >= 100:
                if rect_100minus.collidepoint(event.pos):
                    bet = bet - 100
                    balance = balance + 100
            if rect_submit.collidepoint(event.pos):
                state = 2
                card_added = False

        # players turn
        if state == 2:
            if not pressed:
                if rect_hit.collidepoint(event.pos):
                    card_added = False
                if rect_stand.collidepoint(event.pos):
                    player_stand = True

        # play again
        if state >= 4:
            if not pressed:
                if rect_playagain.collidepoint(event.pos):
                    state = 1
                    deck = []
                    ddeck = []
                    score = 0
                    dscore = 0
                    bet = 0
                    money_delt = False

        pressed = True
    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        pressed = False

    # player's turn
    if state == 2:
        if score == 21:
            state = 4
        else:
            if score < 21:
                if not card_added:
                    deck = shuffle_add(deck)
                    score = count_score(deck)
                    card_added = True
                    state = 3
                if player_stand:
                    state = 3
                if score > 21:
                    print("player got above 21")
                    state = 5

    # dealers turn
    if state == 3:
        if dscore <= 17:
            if not dealer_hit:
                dealer_hit = True
                timer = 0
        else:
            if not dealer_stand:
                dealer_stand = True
                timer = 0
        if dealer_hit and timer >= 900:
            ddeck = shuffle_add(ddeck)
            dscore = count_score(ddeck)
            state = 2
            dealer_hit = False
        if dealer_stand and timer >= 900:
            state = 2
            dealer_stand = False
            if player_stand:
                if score == dscore:
                    print("you both got less then 21 and it is a draw")
                    state = 6
                else:
                    if score < dscore:
                        print("you both got less then 21 but dealer still won")
                        state = 5
                    else:
                        state = 4
                        print("you both got less then 21 but you still won")

        if dscore > 21:
            print("Dealer lost")
            state = 4

    if state == 4 and not money_delt:
        balance = balance + (bet * 2)
        bet = 0
        money_delt = True
    if state == 5 and not money_delt:
        bet = 0
        money_delt = True
    if state == 6 and not money_delt:
        bet = 0
        balance = balance + bet

    # drawing

    screen.fill((37, 105, 21))
    draw_image("Images/background.jpg", 0, 0, 0.6)  # background

    # state 0
    if state == 0:
        draw_image_c("Images/blackjack_main (Small).png", screen_w, screen_h - 180, 1)
        if rect_play.collidepoint(mouse_pos):
            draw_image("Images/play.png", 649 - 12, 580 - 5, 1.1)
        else:
            draw_image("Images/play.png", 649, 580, 1)

    if state >= 1:
        # draw player cards
        for i in range(0, len(deck)):
            draw_image("Cards/" + deck[i] + ".png", 300 + i * 190, 550, 1)

        # draw dealer cards
        for i in range(0, len(ddeck)):
            draw_image("Cards/" + ddeck[i] + ".png", 300 + i * 190, 30, 1)

        # buttons
        if rect_hit.collidepoint(mouse_pos):
            draw_image("Images/wood_button_hit_d.png", 30, 550, 1)
        else:
            draw_image("Images/wood_button_hit.png", 30, 550, 1)
        if rect_stand.collidepoint(mouse_pos):
            draw_image("Images/wood_button_stand_d.png", 30, 700, 1)
        else:
            draw_image("Images/wood_button_stand.png", 30, 700, 1)

        # players score
        draw_image("Images/wood_board.png", 1250, 540, 1)
        draw_text(score, 1250, 540, 280, 280, 20, 20, 20, 64)

        # dealers score
        draw_image("Images/wood_board.png", 1250, 20, 1)
        draw_text(dscore, 1250, 20, 280, 280, 20, 20, 20, 64)

        draw_image("Images/wide_board.png", 570, 345, 1)
        draw_text("Current bet:", 618, 280, 300, 100, 180, 180, 180, 28)

        # blinking bet display
        if state == 1:
            if rect_submit.collidepoint(mouse_pos):
                draw_text(str(bet) + " $", 618, 360, 300, 100, 255, 255, 255, 90)
            else:
                if timer >= 500:
                    draw_text(str(bet) + " $", 618, 360, 300, 100, 230, 184, 21, 80)
                else:
                    draw_text(str(bet) + " $", 618, 360, 300, 100, 255, 255, 255, 80)
        else:
            draw_text(str(bet) + " $", 618, 360, 300, 100, 255, 255, 255, 80)

        # Displays what state it is
        draw_text(states[state], 618, 430, 300, 100, 30, 30, 30, 20)

        draw_image("Images/wide_board.png", 1250, 300, 0.7)
        draw_text(str(balance) + " $", 1305, 300, 280, 88, 255, 255, 255, 30)
        draw_text("Bank:", 1175, 300, 280, 88, 41, 28, 13, 30)

        # all in button
        if rect_allin.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (109, 73, 26), rect_allin, border_radius=20)
            pygame.draw.rect(screen, (61, 48, 33), rect_allin, 3, border_radius=20)
            draw_text("All in", 1250, 390, 135, 44, 230, 230, 230, 24)
        else:
            pygame.draw.rect(screen, (99, 63, 16), rect_allin, border_radius=20)
            pygame.draw.rect(screen, (51, 38, 23), rect_allin, 3, border_radius=20)
            draw_text("All in", 1250, 390, 135, 44, 41, 28, 13, 24)

        # all out button
        if rect_allout.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (109, 73, 26), rect_allout, border_radius=20)
            pygame.draw.rect(screen, (61, 48, 33), rect_allout, 3, border_radius=20)
            draw_text("All out", 1395, 390, 135, 44, 230, 230, 230, 24)
        else:
            pygame.draw.rect(screen, (99, 63, 16), rect_allout, border_radius=20)
            pygame.draw.rect(screen, (51, 38, 23), rect_allout, 3, border_radius=20)
            draw_text("All out", 1395, 390, 135, 44, 41, 28, 13, 24)

        # hald button
        if rect_half.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (109, 73, 26), rect_half, border_radius=20)
            pygame.draw.rect(screen, (61, 48, 33), rect_half, 3, border_radius=20)
            draw_text("Half", 1250, 440, 280, 44, 230, 230, 230, 24)
        else:
            pygame.draw.rect(screen, (99, 63, 16), rect_half, border_radius=20)
            pygame.draw.rect(screen, (51, 38, 23), rect_half, 3, border_radius=20)
            draw_text("Half", 1250, 440, 280, 44, 51, 38, 23, 24)

        # +100 button
        if rect_100plus.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (109, 73, 26), rect_100plus, border_radius=20)
            pygame.draw.rect(screen, (61, 48, 33), rect_100plus, 3, border_radius=20)
            draw_text("+100", 1250, 490, 135, 44, 230, 230, 230, 24)
        else:
            pygame.draw.rect(screen, (99, 63, 16), rect_100plus, border_radius=20)
            pygame.draw.rect(screen, (51, 38, 23), rect_100plus, 3, border_radius=20)
            draw_text("+100", 1250, 490, 135, 44, 51, 38, 23, 24)

        # -100 button
        if rect_100minus.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (109, 73, 26), rect_100minus, border_radius=20)
            pygame.draw.rect(screen, (61, 48, 33), rect_100minus, 3, border_radius=20)
            draw_text("-100", 1395, 490, 135, 44, 230, 230, 230, 24)
        else:
            pygame.draw.rect(screen, (99, 63, 16), rect_100minus, border_radius=20)
            pygame.draw.rect(screen, (51, 38, 23), rect_100minus, 3, border_radius=20)
            draw_text("-100", 1395, 490, 135, 44, 51, 38, 23, 24)

        draw_image("Images/dealer.png", 20, 20, 1)

        if state >= 4:
            # rect_playagain=pygame.Rect(468, 600, 600, 100)
            pygame.draw.rect(screen, (109, 73, 26), rect_playagain, border_radius=5)
            draw_text("Play Again", 468, 600, 600, 100, 51, 38, 23, 64)

    pygame.display.flip()


pygame.quit()
