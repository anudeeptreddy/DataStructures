# python2
import random


def read_input():
    return raw_input().rstrip(), raw_input().rstrip()


def print_occurrences(output):
    print ' '.join(map(str, output))


def get_occurrences_naive(pattern, text):
    return [
        i
        for i in range(len(text) - len(pattern) + 1)
        if text[i:i + len(pattern)] == pattern
    ]


def string_hash(s, prime, multiplier):
    result = 0
    for c in reversed(s):
        result = (result * multiplier + ord(c)) % prime
    return result


def pre_compute_hashes(text, len_p, p, x):
    H = [0] * (len(text) - len_p + 1)
    s = text[-len_p:]
    H[len(text)-len_p] = string_hash(s, p, x)
    y = 1
    for i in range(1, len_p+1):
        y = (y * x) % p
    for i in reversed(range(len(text) - len_p)):
        pre_hash = x * H[i + 1] + ord(text[i]) - y * ord(text[i + len_p])
        while pre_hash < 0:
            pre_hash += p
        H[i] = pre_hash % p
    return H


def get_occurrences_rabinkarp(pattern, text):
    # Rabin Karp algorithm to find all the indices of a pattern P in text T
    len_p = len(pattern)
    p = 1000000003
    x = random.randint(1, p)

    hash_p = string_hash(pattern, p, x)
    H = pre_compute_hashes(text, len_p, p, x)
    return [
        i
        for i in range(len(text) - len(pattern) + 1)
        if hash_p == H[i] and text[i:i + len(pattern)] == pattern
    ]


if __name__ == '__main__':
    print_occurrences(get_occurrences_rabinkarp(*read_input()))


# i/p
# aba
# abacaba
#
# o/p
# 0 4