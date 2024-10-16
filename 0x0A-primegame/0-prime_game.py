#!/usr/bin/python3
"""Module for determining winners"""


def sieve_of_eratosthenes(n):
    """
    This function generates all prime numbers up to n
    using the Sieve of Eratosthenes method.
    It returns a list where the index represents a number,
    and the value at that index is True if the number is prime,
    False otherwise.
    """
    # Initialize a list with True values
    # assuming every number is prime initially
    sieve = [True] * (n + 1)

    # 0 and 1 are not prime numbers, so we mark them as False
    sieve[0] = sieve[1] = False

    # Start marking multiples of each prime number as False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:  # If i is still marked as prime
            # Mark all multiples of i as non-prime (i.e., False)
            for multiple in range(i * i, n + 1, i):
                sieve[multiple] = False

    # Return the list where prime numbers
    # are True and non-prime numbers are False
    return sieve


def count_primes_up_to(n, primes):
    """
    This function counts how many prime numbers are up to n,
    given a list of prime status (True or False).
    It returns the count of primes between 2 and n (inclusive).
    """
    # Count all numbers that are prime up to n
    return sum(1 for i in range(2, n + 1) if primes[i])


def isWinner(x, nums):
    """
    This function determines the overall
    winner after x rounds of the prime game.
    Args:
    x: The number of rounds.
    nums: A list where each element is the number n
    representing the size of the set of numbers [1, 2, ..., n].

    Returns:
    "Maria" if Maria wins the most rounds,
    "Ben" if Ben wins the most rounds,
    or None if they win the same number of rounds.
    """
    # Edge case: If there are no rounds or nums
    # list is empty, return None (no winner)
    if not nums or x < 1:
        return None

    # Find the maximum n from the nums list
    # so we know how many primes to calculate
    max_n = max(nums)

    # Generate a list of primes up to the
    # largest n using the Sieve of Eratosthenes
    primes = sieve_of_eratosthenes(max_n)

    # Create an array to store how many prime numbers
    # exist up to each number from 1 to max_n
    prime_count = [0] * (max_n + 1)

    # Populate the prime_count array
    for i in range(1, max_n + 1):
        # The number of primes up to i is the number
        # of primes up to (i - 1) plus 1 if i is prime
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    # Track the number of wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    # Go through each round and determine the winner
    for n in nums:
        # If the number of primes up to n is odd,
        # Maria wins (since she goes first)
        # If the number of primes up to n is even, Ben wins
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine who won the most rounds
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
