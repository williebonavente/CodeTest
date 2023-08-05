def longest_repeated_substring(string):
    n = len(string)
    suffixes = [(string[i:], i) for i in range(n)]
    suffixes.sort()
    lcp = [0] * n
    for i in range(1, n):
        j = 0
        while suffixes[i - 1][0][j] == suffixes[i][0][j]:
            j += 1
        lcp[i] = j
    max_length = max(lcp)
    end_index = lcp.index(max_length)
    return string[suffixes[end_index][1]:suffixes[end_index][1] + max_length]
