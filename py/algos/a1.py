import sys

def median(nums: list[int]) -> int | float:
    """
    Find median of a list of numbers.
    Wiki: https://en.wikipedia.org/wiki/Median

    Args:
        nums: List of numbers

    Returns:
        Median.
    """
    sorted_list = sorted(nums)
    length = len(sorted_list)
    mid_index = length // 2
    return (
        (sorted_list[mid_index] + sorted_list[mid_index - 1]) / 2
        if length % 2 == 0
        else sorted_list[mid_index]
    )


def main():
    # Check if the user provided arguments
    if len(sys.argv) <= 1:
        print("Usage: python median.py <num1> <num2> <num3> ...")
        return

    # Parse command-line arguments to integers
    try:
        nums = [int(arg) for arg in sys.argv[1:]]
    except ValueError:
        print("Invalid input. Please provide only integer values.")
        return

    result = median(nums)
    print(f"Median: {result}")


if __name__ == "__main__":
    main()
