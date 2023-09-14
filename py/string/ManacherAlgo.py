def manacher_algorithm(string):
    modified_string = '#'.join('^{}$'.format(string))
    n = len(modified_string)
    p = [0] * n
    center = right = 0
    
    for i in range(1, n - 1):
        if i < right:
            mirror = 2 * center - i
            p[i] = min(right - i, p[mirror])
        
        while modified_string[i + p[i] + 1] == modified_string[i - p[i] - 1]:
            p[i] += 1
        
        if i + p[i] > right:
            center = i
            right = i + p[i]
    
    max_length = max(p)
    center_index = p.index(max_length)
    start_index = (center_index - max_length) // 2
    end_index = start_index + max_length
    
    longest_palindrome = string[start_index:end_index]
    return longest_palindrome

if __name__ == "__main__":
    input_string = "babad"
    result = manacher_algorithm(input_string)
    print("Longest palindromic substring:", result)
