def zlw_compress(data):
    compressed_data = []
    dictionary = {}

    i = 0
    while i < len(data):
        current = data[i]
        j = i + 1
        while j < len(data) and current + data[j] in dictionary:
            current += data[j]
            j += 1

        compressed_data.append(dictionary.get(current, current))
        dictionary[current] = len(dictionary) + 1

        i = j

    return compressed_data
