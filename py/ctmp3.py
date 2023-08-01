import random

def fisher_yates_shuffle(list):
    """
    Randomly shuffle a list.

    Args:

    list: The list to be shuffled.

    Returns
        The shuffled list.

    """
    
    for i in range(len(list) - 1):
        j = random.randint(i, len(list) - 1)
        list[i], list[j]  = list[j], list[i]
    
    return list

if __name__ == "__main__":
    list = [1, 2, 3, 4, 5]
    print(fisher_yates_shuffle(list))
    