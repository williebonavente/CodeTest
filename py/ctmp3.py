import random
from typing import List

def fisher_yates_shuffle(deck: List[str]) -> List[str]:
    """
    Randomly shuffle a deck of cards using the Fisher-Yates algorithm.

    Args:
        deck (List[str]): The list of cards representing the deck.

    Returns:
        List[str]: The shuffled deck of cards.
    """
    n = len(deck)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        deck[i], deck[j] = deck[j], deck[i]
    
    return deck

if __name__ == "__main__":
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck_of_cards = [rank + ' of ' + suit for rank in ranks for suit in suits]
    
    print("Original deck of cards:")
    print(deck_of_cards)

    shuffled_deck = fisher_yates_shuffle(deck_of_cards)

    print("\nShuffled deck of cards:")
    print(shuffled_deck)
