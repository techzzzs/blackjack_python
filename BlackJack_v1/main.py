import pygame
import sys
from card_randomizer import shuffle_add, count_score
from draw import draw_text, draw_image, draw_image_c

pygame.init()
pygame.mixer.init()

# -----------------------------------------------------
# WINDOW
# -----------------------------------------------------
screen_w, screen_h = 1536, 793
screen = pygame.display.set_mode((screen_w, screen_h), pygame.RESIZABLE | pygame.WINDOWMAXIMIZED)
pygame.display.set_caption("BlackJack")
clock = pygame.time.Clock()

# -----------------------------------------------------
# SOUND CACHE
# -----------------------------------------------------
sounds = {}
def play(path):
    if path not in sounds:
        sounds[path] = pygame.mixer.Sound("Sounds/" + path)
    sounds[path].play()

# -----------------------------------------------------
# RECTANGLES
# -----------------------------------------------------
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

# -----------------------------------------------------
# GAME STATE
# -----------------------------------------------------
state = 0
states = {
    0: "Main menu",
    1: "Place your bet",
    2: "Your turn",
    3: "Dealer's turn",
    4: "You Won",
    5: "You Lost",
    6: "Draw"
}

deck = []
ddeck = []
bet = 0
balance = 10000
dealer_has_hole = True  # dealer starts with one visible card

mouse_down = False
mouse_clicked = False

# -----------------------------------------------------
# MAIN LOOP
# -----------------------------------------------------
running = True
while running:
    dt = clock.tick(60)
    mouse_pos = pygame.mouse.get_pos()
    mouse_clicked = False

    # ---------------- EVENTS ----------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_down = True
            mouse_clicked = True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            mouse_down = False

    # ---------------- STATE 0 — MAIN MENU ----------------
    if state == 0:
        if mouse_clicked and rect_play.collidepoint(mouse_pos):
            play("button.mp3")
            state = 1

    # ---------------- STATE 1 — BETTING ----------------
    if state == 1:
        if mouse_clicked:
            # Remove all
            if rect_allout.collidepoint(mouse_pos) and bet > 0:
                play("button.mp3")
                balance += bet
                bet = 0
            # All in
            if rect_allin.collidepoint(mouse_pos) and balance > 0:
                play("button.mp3")
                bet += balance
                balance = 0
            # Half
            if rect_half.collidepoint(mouse_pos) and balance > 0:
                play("button.mp3")
                half = round(balance / 2)
                bet += half
                balance -= half
            # +100
            if rect_100plus.collidepoint(mouse_pos) and balance >= 100:
                play("button.mp3")
                bet += 100
                balance -= 100
            # -100
            if rect_100minus.collidepoint(mouse_pos) and bet >= 100:
                play("button.mp3")
                bet -= 100
                balance += 100
            # Submit
            if rect_submit.collidepoint(mouse_pos) and bet > 0:
                play("coin_long.mp3")
                # Reset decks
                deck = []
                ddeck = []
                dealer_has_hole = True
                # Player gets 2 cards
                deck = shuffle_add(deck)
                deck = shuffle_add(deck)
                # Dealer gets 1 card (second is hidden)
                ddeck = shuffle_add(ddeck)
                state = 2

    # ---------------- STATE 2 — PLAYER TURN ----------------
    if state == 2:
        score = count_score(deck)
        if score > 21:
            state = 5  # player bust

        if mouse_clicked:
            # Hit
            if rect_hit.collidepoint(mouse_pos):
                play("button.mp3")
                deck = shuffle_add(deck)
                score = count_score(deck)
                if score > 21:
                    state = 5
            # Stand
            if rect_stand.collidepoint(mouse_pos):
                play("button.mp3")
                # Reveal dealer's hidden card
                if dealer_has_hole:
                    ddeck = shuffle_add(ddeck)
                    dealer_has_hole = False
                state = 3

    # ---------------- STATE 3 — DEALER TURN ----------------
if state == 3:
    dscore = count_score(ddeck)

    # Reveal the hidden card only once
    if dealer_has_hole:
        ddeck = shuffle_add(ddeck)
        dealer_has_hole = False

    # Dealer hits ONE card per frame (safe!) instead of freezing the loop
    if dscore < 17:
        dealer_hit_timer = pygame.time.get_ticks()  # create delay
        if not hasattr(state, "last_hit") or pygame.time.get_ticks() - state.last_hit > 300:
            ddeck = shuffle_add(ddeck)
            state.last_hit = pygame.time.get_ticks()
    else:
        # Evaluate result once dealer is done
        score = count_score(deck)
        if dscore > 21 or score > dscore:
            state = 4
        elif score < dscore:
            state = 5
        else:
            state = 6


    # ---------------- PAYOUTS ----------------
    if state == 4:  # win
        balance += bet * 2
        bet = 0
    if state == 5:  # lose
        bet = 0
    if state == 6:  # draw
        balance += bet
        bet = 0

    # ---------------- PLAY AGAIN ----------------
    if state >= 4 and mouse_clicked and rect_playagain.collidepoint(mouse_pos):
        play("button.mp3")
        state = 1
        deck = []
        ddeck = []
        bet = 0
        dealer_has_hole = True

    # ---------------- DRAW ----------------
    screen.fill((37, 105, 21))
    draw_image(screen, "Images/background.jpg", 0, 0, 0.6)

    # Main menu
    if state == 0:
        draw_image_c(screen, "Images/blackjack_main (Small).png", screen_w, screen_h, 1)
        if rect_play.collidepoint(mouse_pos):
            draw_image(screen, "Images/play.png", 649 - 12, 580 - 5, 1.1)
        else:
            draw_image(screen, "Images/play.png", 649, 580, 1)

    # Game UI (betting + gameplay)
    if state >= 1:
        # Player cards
        for i, card in enumerate(deck):
            draw_image(screen, f"Cards/{card}.png", 300 + i * 190, 550, 1)
        # Dealer cards
        for i, card in enumerate(ddeck):
            draw_image(screen, f"Cards/{card}.png", 300 + i * 190, 30, 1)
        # Dealer character
        draw_image(screen, "Images/dealer.png", 20, 20, 1)
        # Player score
        draw_image(screen, "Images/wood_board.png", 1250, 540, 1)
        draw_text(screen, count_score(deck), 1250, 540, 280, 280, 20, 20, 20, 64)
        # Dealer score
        draw_image(screen, "Images/wood_board.png", 1250, 20, 1)
        draw_text(screen, count_score(ddeck), 1250, 20, 280, 280, 20, 20, 20, 64)
        # Betting UI
        draw_image(screen, "Images/wide_board.png", 570, 345, 1)
        draw_text(screen, f"Current bet: {bet} $", 618, 280, 300, 100, 180, 180, 180, 28)
        draw_image(screen, "Images/wide_board.png", 1250, 300, 0.7)
        draw_text(screen, f"{balance} $", 1305, 300, 280, 88, 255, 255, 255, 30)
        draw_text(screen, "Bank:", 1175, 300, 280, 88, 41, 28, 13, 30)
        # Betting buttons
        draw_text(screen, "All in", 1250, 390, 135, 44, 41, 28, 13, 24)
        draw_image(screen, "Images/wood_board.png",1250, 390, 1,)
        draw_text(screen, "All out", 1395, 390, 135, 44, 41, 28, 13, 24)
        draw_text(screen, "Half", 1250, 440, 280, 44, 51, 38, 23, 24)
        draw_text(screen, "+100", 1250, 490, 135, 44, 51, 38, 23, 24)
        draw_text(screen, "-100", 1395, 490, 135, 44, 51, 38, 23, 24)
        # Hit/Stand buttons
        draw_text(screen, "Hit", 30, 550, 225, 125, 255, 255, 255, 32)
        draw_text(screen, "Stand", 30, 700, 225, 125, 255, 255, 255, 32)
        # Play Again button
        if state >= 4:
            pygame.draw.rect(screen, (109, 73, 26), rect_playagain, border_radius=5)
            draw_text(screen, "Play Again", 468, 600, 600, 100, 51, 38, 23, 64)

    pygame.display.flip()

pygame.quit()