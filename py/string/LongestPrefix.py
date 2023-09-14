def longest_common_prefix_array(string):
    n = len(string)
    suffixes = [(string[i:], i) for i in range(n)]
    suffixes.sort()
    lcp = [0] * n
    for i in range(1, n):
        j = 0
        while suffixes[i - 1][0][j] == suffixes[i][0][j]:
            j += 1
        lcp[i] = j
    return lcp
