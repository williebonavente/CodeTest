import random
from typing import List

def fisher_yates_shuffle(lst: List[int]) -> List[int]:
    """
    Randomly shuffle a list using the Fisher-Yates algorithm.

    Args:
        lst: The list to be shuffled.

    Returns:
        The shuffled list.
    """
    for i in range(len(lst) - 1, 0, -1):
        j = random.randint(0, i)
        lst[i], lst[j] = lst[j], lst[i]
    
    return lst

def random_permutation_test(group_a: List[float], group_b: List[float], num_permutations: int) -> float:
    """
    Perform random permutation testing to compare the means of two groups.

    Args:
        group_a: List of test scores for Group A.
        group_b: List of test scores for Group B.
        num_permutations: Number of random permutations to perform.

    Returns:
        The p-value indicating the significance of the difference between the two groups.
    """
    observed_difference = abs(sum(group_a) / len(group_a) - sum(group_b) / len(group_b))
    combined_scores = group_a + group_b
    count_greater = 0

    for _ in range(num_permutations):
        shuffled_scores = fisher_yates_shuffle(combined_scores)
        new_group_a = shuffled_scores[:len(group_a)]
        new_group_b = shuffled_scores[len(group_a):]
        permutation_difference = abs(sum(new_group_a) / len(new_group_a) - sum(new_group_b) / len(new_group_b))
        if permutation_difference >= observed_difference:
            count_greater += 1

    p_value = count_greater / num_permutations
    return p_value

if __name__ == "__main__":
    group_a = [85, 90, 78, 92, 88]
    group_b = [79, 84, 82, 88, 81]
    num_permutations = 10000

    p_value = random_permutation_test(group_a, group_b, num_permutations)
    print(f"P-value: {p_value}")
