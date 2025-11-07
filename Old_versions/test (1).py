import random
import time
import pygame
from draw import draw_text, draw_image

# draw_text(text, x, y, width, hight, red, green, blue)
# draw_image(file, x, y, scale)


def pullRandomCard(cardValues):
    return random.choice(list(cardValues.keys()))


def calculate_hand(hand):
    total = sum(cardValues[card] for card in hand)
    aces = hand.count("cardace")
    while total > 21 and aces > 0:
        total -= 10  # Count one ace as 1 instead of 11
        aces -= 1
    return total


def showCards():
    print(
        "Your starting hand: ",
        startingHand,
        calculate_hand(startingHand),
        "\n",
        "Dealers hand: ",
        dealerHand,
        calculate_hand(dealerHand),
        "\n",
        "your current moneys cuh: ",
        currentCurrency,
    )


def delay_action(delay_ms, callback=None):
    """Delay wrapper that uses sleep for terminal but can be adapted for Tkinter later."""
    time.sleep(delay_ms / 1000.0)
    if callback:
        callback()


Winnings = 2
currentCurrency = 100

cardace1 = 1
cardValues = {
    "card2": 2,
    "card3": 3,
    "card4": 4,
    "card5": 5,
    "card6": 6,
    "card7": 7,
    "card8": 8,
    "card9": 9,
    "card10": 10,
    "cardjack": 10,
    "cardqueen": 10,
    "cardking": 10,
    "cardace": 11,
}
gamestate = 3
# gamestate = 0 nozime ending screen
# gamestate = 1 nozime player gajiens
# gamestate = 2 nozime dealera gajiens
# gamestate = 3 nozime betting round
startingHand = []
dealerHand = []

# window settings
screen_width = 1000
screen_hight = 600
screen = pygame.display.set_mode((screen_width, screen_hight))
clock = pygame.time.Clock()
pygame.display.set_caption("BlackJack")

pygame.init()
running = True

# game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #screen.fill((37, 105, 21))
    draw_image("Images/background.jpg", 0, 0, 0.37)
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()[0]

    if gamestate == 1:
        if calculate_hand(startingHand) == 21:
            print("blackjack!")
            currentCurrency = currentCurrency + (bet * 2)
            print(
                "your new cash rn is:",
                currentCurrency,
                "  (fuckin hell you rich as fuck)",
            )
            gamestate = 0
        else:

            if action == "hit":
                startingHand.append(pullRandomCard(cardValues))
                showCards()
                if calculate_hand(startingHand) > 21:
                    print("you lose fuckin lmao")
                    gamestate = 0

            elif action == "stand":
                gamestate = 2
            else:
                print(
                    "invalid input cuh (write either hit or stand with lowercase letters)"
                )

    # Dealer's turn
    if gamestate == 2:
        print("Dealers move")
        dealerHand.append(pullRandomCard(cardValues))
        showCards()

    if gamestate == 2:
        if calculate_hand(dealerHand) == 21:
            print("You lost lmao dealer had blackjack")
            gamestate = 0

        elif calculate_hand(dealerHand) < 17:
            dealerHand.append(pullRandomCard(cardValues))
            showCards()
        elif calculate_hand(dealerHand) >= 17 and calculate_hand(dealerHand) < 21:
            if calculate_hand(dealerHand) < calculate_hand(startingHand):
                print("Great job you beat the deala")
                currentCurrency = currentCurrency + (bet * 2)
                print(
                    "your new cash rn is:",
                    currentCurrency,
                    "  (fuckin hell you rich as fuck)",
                )
                gamestate = 0
            elif calculate_hand(startingHand) < calculate_hand(dealerHand):
                print("lmao you lose cuh")
                gamestate = 0
            else:
                print("oh shi thas a draw bro")
                currentCurrency = currentCurrency + bet
                gamestate = 0
        elif calculate_hand(dealerHand) > 21:
            print("you won cuh!")
            currentCurrency = currentCurrency + (bet * 2)
            print(
                "your new cash rn is:",
                currentCurrency,
                "  (fuckin hell you rich as fuck)",
            )
            gamestate = 0

    if gamestate == 0:
        if currentCurrency == 0:
            print(
                "maan im sorry but you broke asl now go and get yo bank up and try again later"
            )
            running = False
        if action2 == "yes":
            gamestate = 3

        elif action2 == "no":
            running = False
        else:
            print("at least give me a normal answer knee guard")

    if gamestate == 3:
        draw_image("Images/wood_board.png", 10, 300, 0.6)
        print("yo current cash brother: ", currentCurrency)
        # action3 = input("enter how much you tryna bet:  ")
        action3 = "0"
        try:
            action3 = int(action3)
        except ValueError:
            print("maaaan enter a numbah cuh (without no decimal points please uwu)")
            continue

        if action3 > currentCurrency or action3 == 0:
            print("maaannn you broke as hell you cant afford to play shittt")
            continue

        bet = action3
        currentCurrency -= bet

        for i in range(2):
            startingHand.append(pullRandomCard(cardValues))
        dealerHand.append(pullRandomCard(cardValues))
        showCards()

    pygame.display.flip()
pygame.quit()
