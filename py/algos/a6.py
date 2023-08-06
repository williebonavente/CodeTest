def van_eck_sequence(n):
    sequence = [0]
    last_occurrence = {0: 0}

    for i in range(1, n):
        if sequence[i - 1] in last_occurrence:
            sequence.append(i - 1 - last_occurrence[sequence[i - 1]])
        else:
            sequence.append(0)

        last_occurrence[sequence[i - 1]] = i - 1

    return sequence
