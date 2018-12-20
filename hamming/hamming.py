def distance(strand_a, strand_b):
    loop_count = 0
    counter = 0
    if len(strand_a) != len(strand_b):
        raise ValueError("Not cool")
    while loop_count < len(strand_a):
        if strand_a[loop_count] != strand_b[loop_count]:
            counter += 1
        loop_count += 1
    return counter

