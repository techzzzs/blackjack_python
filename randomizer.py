import random

numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "ace", "jack", "king", "queen"]
signs = ["c", "d", "h", "s"]

max_cards = len(numbers) * len(signs)


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
    if len(cards) < max_cards:
        done = 0
        while done == 0:
            card = random.choice(numbers) + "_of_" + random.choice(signs)
            if card in cards:
                pass
            else:
                testscore=count_score(cards)
                split = card.split("_")
                
                
                if split[0] == "ace":
                    if testscore <=10:
                        cards.append("ace"+"_"+split[1]+"_"+split[2])
                        done = 1
                    else: 
                        cards.append("aoe"+"_"+split[1]+"_"+split[2])
                        done = 1
                else:
                    cards.append(card)
                    done = 1
    else:
        print("All cards used")
    return cards


def shuffle_remove(prev_deck):
    cards = prev_deck
    if len(cards) >= 1:
        cards.pop()
    return cards




cardvalues = {
    "1_": 1,
    "2_": 2,
    "3_": 3,
    "4_": 4,
    "5_": 5,
    "6_": 6,
    "7_": 7,
    "8_": 8,
    "9_": 9,
    "10": 10,
    "ac": 11,
    "ja": 10,
    "ki": 10,
    "qu": 10,
    "ao": 1,
}

def count_score(deck, first_hidden=False):
    score = 0
    aces = 0

    start = 1 if first_hidden else 0

    for i in range(start, len(deck)):
        card = deck[i][0:2]
        if card == "ac":
            score += 11 
            aces += 1
        else:
            score += cardvalues.get(card, 0)

    while score > 21 and aces > 0:
        score -= 10 
        aces -= 1

    return score
