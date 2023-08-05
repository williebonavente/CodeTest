def burrows_wheeler_transform(string):
    n = len(string)
    rotations = [string[i:] + string[:i] for i in range(n)]
    rotations.sort()
    return ''.join([rotation[-1] for rotation in rotations])
