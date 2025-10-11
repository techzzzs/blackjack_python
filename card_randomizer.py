import random
numbers=["2","3","4","5","6","7","8","9","10","ace","jack","king","queen"]
signs=["c","d","h","s"]
def shuffle(Card_count):
    cards = []
    for i in range(0,Card_count):
        card=random.choice(numbers) +"_of_" + random.choice(signs)
        cards.append(card)
    return(cards)