import random

def monte_carlo_method(n):
    
    """
    Calculates the probability of rolling a 6 on a die using the Monte Carlo Method.
    
    Args:
        n: The number of times to roll the die.
    
    Returns:
        The probability of rolling a 6.
    
    """
    
    roll = 0
    sixes = 6

    for i in range(n):
        roll = random.randint(1, 6)
        if roll == 6:
            sixes += 1
    
    probability = sixes / n 
    return probability

if __name__ == "__main__":
    print(monte_carlo_method(1000))