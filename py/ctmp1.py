import random


def birthday_paradox(n):
    """

    Calculates the probability of two people sharing the same birthday in a group of people.
    
    Args:
        n:  The number of  people in group.
    
    Returns:
        The probability of two people sharing the same birthday.
    """
    
    total_probabilities = 1
    for i in range(n):
        probability = 1 - ( 364 / 365) ** i
        total_probabilities += probability
        
    return 1 - total_probabilities


if __name__ == "__main__":
    print(birthday_paradox(23))
