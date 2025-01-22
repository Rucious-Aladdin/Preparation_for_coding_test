from collections import defaultdict
import math

def euler(num, *args):
    val = num
    for factor in args:
        val = val * (factor - 1) // factor
    return val

if __name__ == "__main__":
    N = int(input())
    orig = N
    factors = defaultdict(int)
    while N != 1:
        for i in range(2, int(math.sqrt(N)) + 1):
            if N % i == 0:
                factors[i] += 1
                N //= i
                break
        else:
            factors[N] += 1
            N = 1

    print(factors)
    factors = factors.keys()
    print(euler(orig, *factors))
    