import random

numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "ace", "jack", "king", "queen"]
signs = ["c", "d", "h", "s"]

max_cards=len(numbers)*len(signs)


def shuffle(Card_count):
    cards = []
    done = 0
    for i in range(0, Card_count):
        while done < Card_count:
            card = random.choice(numbers) + "_of_" + random.choice(signs)
            if card in cards:
                pass
            else:
                cards.append(card)
                done = done + 1
    return cards


def shuffle_add(prev_deck):
    cards = prev_deck
    if len(cards)<max_cards:
        done = 0
        while done ==0:
            card = random.choice(numbers) + "_of_" + random.choice(signs)
            if card in cards:
                pass
            else:
                cards.append(card)
                done=1
    else:
        print("All cards used")
    return cards


def shuffle_remove(prev_deck):
    cards = prev_deck
    if len(cards)>=1:
        cards.pop()
    return cards
