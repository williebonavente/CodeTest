def find_duplicate_characters(string):
    duplicates = []
    for char in string:
        if string.count(char) > 1 and char not in duplicates:
            duplicates.append(char)
    return duplicates
