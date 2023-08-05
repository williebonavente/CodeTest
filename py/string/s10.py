def rabin_karp_search(text, pattern):
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1

    # Calculate h as (d^(m-1)) % q
    for i in range(m - 1):
        h = (h * d) % q

    # Calculate hash value for pattern and the first window of text
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    # Slide the pattern over the text and check for matches
    for i in range(n - m + 1):
        if p == t:
            # Check if characters in current window match the pattern
            for j in range(m):
                if text[i + j] != pattern[j]:
                    break
            else:
                return i  # Pattern found at index i

        # Calculate hash value for next window of text
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q

    return -1  # Pattern not found

# Example usage
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
index = rabin_karp_search(text, pattern)
if index != -1:
    print(f"Pattern found at index {index}")
else:
    print("Pattern not found")
