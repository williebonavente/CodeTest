def reverse_string_recursive(string):
    if len(string) == 0:
        return string
    else:
        return reverse_string_recursive(string[1:]) + string[0]
