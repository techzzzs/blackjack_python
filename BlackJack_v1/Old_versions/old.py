
import random
import tkinter as tk
""""root = tk.Tk()
root.title("Blackjack")
root.geometry("800x600")
root.mainloop()"""

def pullRandomCard(cardValues):
    return random.choice(list(cardValues.keys()))

def startHand(handSize, cardValues):
    hand = []
    for i in range(handSize):
        hand.append(pullRandomCard(cardValues))
    return hand
cardace1 = 1
cardValues = {
    "card2" : 2,
    "card3" : 3,
    "card4" : 4,
    "card5" : 5,
    "card6" : 6,
    "card7" : 7,
    "card8" : 8,
    "card9" : 9,
    "card10" : 10,
    "cardjack" : 10,
    "cardqueen" : 10,
    "cardking" : 10,
    "cardace" : 11,
}
startingHand = []
dealerHand = []
for i in range(2):
    startingHand.append(pullRandomCard(cardValues))
for i in range(1):
    dealerHand.append(pullRandomCard(cardValues))
print("Your starting hand: ",startingHand, sum(cardValues[card] for card in startingHand),"\n","Dealers hand: ", dealerHand, sum(cardValues[card] for card in dealerHand))
if sum(cardValues[card] for card in startingHand) == 21:
    print("balckerjackers")
while sum(cardValues[card] for card in startingHand) < 21:
    print("you staying or hitting fellow gambler?")
    action = input("raksti hit vai stand:")
    if action == "hit":
        startingHand.append(pullRandomCard(cardValues))
        print(startingHand, sum(cardValues[card] for card in startingHand))
    elif action == "stand":
        print(startingHand, sum(cardValues[card] for card in startingHand))
        while sum(cardValues[card] for card in dealerHand) < 17:
            dealerHand.append(pullRandomCard(cardValues))
        print(dealerHand, sum(cardValues[card] for card in dealerHand))

        if sum(cardValues[card] for card in dealerHand) > 21 and cardace1 in dealerHand:
            dealerHand.remove("cardace1")
            dealerHand.append("cardace1")







        if sum(cardValues[card] for card in dealerHand) > 21 or sum(cardValues[card] for card in startingHand) > sum(cardValues[card] for card in dealerHand):
            print("you win")
        elif sum(cardValues[card] for card in startingHand) < sum(cardValues[card] for card in dealerHand):
            print("you lose")
        elif sum(cardValues[card] for card in startingHand) == sum(cardValues[card] for card in dealerHand):
            print("draw")
        break

if sum(cardValues[card] for card in startingHand) > 21:
    print("busted")
