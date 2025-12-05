import random

numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "ace", "jack", "king", "queen"]
signs = ["c", "d", "h", "s"]

max_cards = len(numbers) * len(signs)

cardvalues = {
    "2_": 2, "3_": 3, "4_": 4, "5_": 5, "6_": 6,
    "7_": 7, "8_": 8, "9_": 9, "10": 10,
    "ac": 11, "ao": 1,
    "ja": 10, "ki": 10, "qu": 10
}


def shuffle(count):
    """Generate a unique deck subset."""
    result = []
    while len(result) < count:
        card = random.choice(numbers) + "_of_" + random.choice(signs)
        if card not in result:
            result.append(card)
    return result


def shuffle_add(deck):
    """Adds a random unused card with correct ACE handling."""
    if len(deck) >= max_cards:
        return deck

    while True:
        num = random.choice(numbers)
        sign = random.choice(signs)
        card = f"{num}_of_{sign}"

        if card in deck:
            continue

        # ACE logic
        if num == "ace":
            score_now = count_score(deck)
            if score_now <= 10:
                deck.append(f"ace_of_{sign}")     # high ace
            else:
                deck.append(f"aoe_of_{sign}")     # low ace (ao)
        else:
            deck.append(card)

        return deck


def shuffle_remove(deck):
    if deck:
        deck.pop()
    return deck


def count_score(deck):
    score = 0
    for c in deck:
        prefix = c[:2]  # "ac", "ao", "10", "ki", etc.
        score += cardvalues.get(prefix, 0)

    return score
