#!/usr/bin/python3
"""Prime Game """


def sieve_of_eratosthenes(max_n):
    """Returns a list of booleans indicating if an index is a prime number."""
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False

    return is_prime


def prime_count_up_to(n, prime_list):
    """Returns the number of primes up to n using the prime list."""
    return sum(prime_list[:n + 1])


def isWinner(x, nums):
    """A function to declare the winner"""
    if x <= 0 or not nums:
        return None

    max_n = max(nums)

    prime_list = sieve_of_eratosthenes(max_n)

    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if prime_list[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count_up_to(n, prime_list) % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
