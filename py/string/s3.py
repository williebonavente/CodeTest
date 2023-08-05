def are_anagrams(string1, string2):
    # Check if the lengths of both strings are equal
    if len(string1) != len(string2):
        return False

    # Create dictionaries to count the occurrences of characters in each string
    count1 = {}
    count2 = {}

    # Count the occurrences of characters in string1
    for char in string1:
        count1[char] = count1.get(char, 0) + 1

    # Count the occurrences of characters in string2
    for char in string2:
        count2[char] = count2.get(char, 0) + 1

    # Compare the dictionaries to check if the strings are anagrams
    return count1 == count2

# Test cases
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False
