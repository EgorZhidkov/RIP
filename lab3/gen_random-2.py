import random

def gen_random(num_count, begin, end):
    A = [0]*num_count
    for i in range(num_count):
        n = random.randint(begin, end)
        A[i] = str(n)
        print(n, end = ',')
    print('')
    print(A)
    return A

gen_random(5, 1, 3)