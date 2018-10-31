from functools import lru_cache, reduce
from itertools import chain, combinations, permutations
from math import sqrt
from operator import mul


def sieve(limit):
    sieve = {n: True for n in range(2, limit + 1)}
    for n in range(2, limit + 1):
        if sieve[n]:
            for a in range(2, limit // n + 1):
                sieve[n * a] = False
    return [k for k, v in sieve.items() if v]


def isprime(num):
    if num < 2:
        return False
    for d in range(2, int(sqrt(num)) + 1):
        if num % d == 0:
            return False
    return True


def get_divisors(num):
    divisors = []
    divisors.extend([1, num])
    for div in range(2, int(sqrt(num)) + 1):
        fac, rem = divmod(num, div)
        if rem == 0:
            divisors.extend([div, fac])
    return divisors


def get_prime_factors(num):
    def get_next_prime(num):
        for div in range(2, int(sqrt(num)) + 1):
            if num % div == 0:
                num = num // div
                return num, div
        return 1, num

    factors = []
    while num != 1:
        num, factor = get_next_prime(num)
        factors.append(factor)
    return factors


def get_coprimes(num):
    return (k for k in range(1, num) if gcf([num, k]) == 1)


def phi(num):
    return len(list(get_coprimes(num)))


@lru_cache()
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def gcf(seq):
    def _gcf(a, b):
        while b:
            a, b = b, a % b
        return a

    return reduce(_gcf, seq)


def lcm(seq):
    def _lcm(a, b):
        return (a * b) // gcf([a, b])

    return reduce(_lcm, seq)


def multiply(seq):
    return reduce(mul, seq)


def powersets(seq, min_length=0, max_length=None):
    if max_length is None:
        max_length = len(seq)
    return chain.from_iterable([combinations(seq, r) for r in range(min_length, max_length + 1)])


def permute(num, r=None):
    if r is None:
        r = len(str(num))
    return (int(''.join(p)) for p in permutations(str(num), r))


def quadratic(a, b, c):
    det = (b ** 2 - 4 * a * c) ** 0.5
    return ((-b - det) / (2 * a)), ((-b + det) / (2 * a))
