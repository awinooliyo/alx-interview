#!/usr/bin/python3
"""Module for determining winners"""


def sieve_of_eratosthenes(max_n):
    """
       Generate a list of boolean values indicating
       whether numbers are prime.
    """
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
    for start in range(2, int(max_n**0.5) + 1):
        if sieve[start]:
            for multiple in range(start*start, max_n + 1, start):
                sieve[multiple] = False
    return sieve


def prime_count_up_to_n(n, primes):
    """Return the count of primes <= n based on the sieve."""
    count = 0
    for i in range(2, n + 1):
        if primes[i]:
            count += 1
    return count


def isWinner(x, nums):
    """Determine who wins the most rounds between Maria and Ben."""
    max_n = max(nums)  # The highest value of n we need to consider
    primes = sieve_of_eratosthenes(max_n)  # Generate prime numbers up to max_n

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = prime_count_up_to_n(n, primes)
        if prime_count % 2 == 1:
            maria_wins += 1  # Maria wins if prime_count is odd
        else:
            ben_wins += 1  # Ben wins if prime_count is even

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    print("Winner:", isWinner(3, [4, 5, 1]))  # Output should be "Ben"
