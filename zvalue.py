def generate_lookup_table(dimensions):
    limit = 2048 // dimentions
    if limit > 32:
        limit = 32
    lookup_table = [[0]*256]*dimensions
    for i in range(dimensions):
        for j in range(256):
            answer = 0
            for k in range(limit):
                answer |= ((j & (1 << k)) << (k*(dimensions-1) + i))
            lookup_table[i][j] = answer
    return lookup_table


def z_value(lookup_table, point, dimensions):
    answer = 0
    rightshift = 32
    for i1 in range(4):
        answer = answer  << dimensions*8
        for i2 in range(dimensions):
            answer |= lookup_table[i2][(point[i2] >> (rightshift -8*i1)) & 0xFF ]
    return answer
