def boyer_moore(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return []
    last = {}
    for i in range(m):
        last[pattern[i]] = i
    i = m - 1
    j = m - 1
    result = []
    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                result.append(i)
                i += m
                j = m - 1
            else:
                i -= 1
                j -= 1
        else:
            if text[i] in last:
                i += m - min(j, 1 + last[text[i]])
            else:
                i += m
            j = m - 1
    return result
