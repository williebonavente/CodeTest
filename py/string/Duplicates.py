def print_duplicates(string):
    duplicates = []
    for char in string:
        if string.count(char) > 1 and char not in duplicates:
            duplicates.append(char)
    return duplicates

# Function Call
