def boyer_moore_search(text, pattern):
    """
    Performs Boyer-Moore search to find the first occurrence of a pattern in the text.

    Args:
        text (str): The text to search within.
        pattern (str): The pattern to search for.

    Returns:
        int: The starting index of the first occurrence of the pattern in the text,
             or -1 if the pattern is not found.
    """
    m = len(pattern)
    n = len(text)

    # Edge case: empty pattern
    if m == 0:
        return 0

    # Initialize last occurrence dictionary for pattern characters
    last = {}
    for k in range(m):
        last[pattern[k]] = k

    i = m - 1
    k = m - 1

    while i < n:
        if text[i] == pattern[k]:
            if k == 0:
                # Pattern found, return the starting index
                return i
            i -= 1
            k -= 1
        else:
            j = last.get(text[i], -1)
            i += m - min(k, j + 1)
            k = m - 1

    # Pattern not found
    return -1

if __name__ == "__main__":
    text = "this is a test text"
    pattern = "test"
    result = boyer_moore_search(text, pattern)
    if result != -1:
        print(f"Pattern found at index {result}.")
    else:
        print("Pattern not found.")
