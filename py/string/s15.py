def suffix_array(string):
    n = len(string)
    suffixes = [(string[i:], i) for i in range(n)]
    suffixes.sort()
    return [suffix[1] for suffix in suffixes]
