import random

def monte_carlo_probability(rolls, target=6):
    """
    Calculates the probability of rolling a specific number on a die using the Monte Carlo Method.

    Args:
        rolls (int): The number of times to roll the die.
        target (int): The number to calculate the probability for. Default is 6.

    Returns:
        float: The probability of rolling the target number.
    """

    successful_rolls = 0

    for _ in range(rolls):
        roll = random.randint(1, 6)
        if roll == target:
            successful_rolls += 1

    probability = successful_rolls / rolls
    return probability

if __name__ == "__main__":
    num_rolls = 1000
    target_number = 6

    probability = monte_carlo_probability(num_rolls, target_number)

    print(f"The probability of rolling a {target_number} on a die after {num_rolls} rolls is: {probability:.4f}")
