# Prime Game

## Introduction

This project implements a competitive game where Maria and Ben take turns picking prime numbers from a set of consecutive integers. They remove the prime number and all its multiples from the set. The player unable to make a valid move loses the game.

This implementation determines the winner of the game by simulating multiple rounds, where `Maria` always goes first, and both players play optimally. The solution uses **efficient prime number identification** (via the **Sieve of Eratosthenes** algorithm) and leverages dynamic programming to improve performance across multiple rounds.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- Your code will be interpreted/compiled on **Ubuntu 20.04 LTS** using `python3` (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- Your code should follow the **PEP 8** style (version 1.7.x)
- All your files must be executable

## Prerequisites

- Python 3.x
- Basic understanding of:
  - **Prime numbers** and algorithms for finding primes
  - **Game theory** for competitive games with two players
  - **Dynamic programming** for memoization and optimizing repeated calculations

## File Structure

```plaintext
.
├── README.md          # This documentation file
├── 0-prime_game.py    # Implementation of the Prime Game
└── main_0.py          # Main file to test the implementation

Full Example:
Let's walk through an example with n = 10 to see how this works:

## Initialize:

- We start with the sieve: [True, True, True, True, True, True, True, True, True, True, True].
- Indices 0 and 1 will be marked as False later since they are not prime.
- First pass (i = 2):

- i = 2 is prime (sieve[2] is True), so we mark all multiples of 2 as False.
- Starting from 2 * 2 = 4, we mark 4, 6, 8, and 10 as False.
- The sieve now looks like: [False, False, True, True, False, True, False, True, False, True, False].
- Second pass (i = 3):

- i = 3 is prime (sieve[3] is True), so we mark all multiples of 3 as False.
- Starting from 3 * 3 = 9, we mark 9 as False.
- The sieve now looks like: [False, False, True, True, False, True, False, True, False, False, False].
- Stop at 4 (i = 4):

- i = 4 is already marked as False (because it's a multiple of 2), so we skip it.
- Since i has reached the square root of 10 (which is about 3), we can stop checking.
## Final Sieve:
- After running this algorithm, the sieve tells us which numbers are prime:

- True at index 2, 3, 5, and 7 means those are prime numbers.
- False elsewhere means those numbers are not prime.
## Summary:
The outer loop iterates over numbers up to the square root of n.
For each prime number i, the inner loop marks all multiples of i as non-prime starting from i * i.
This efficiently marks all non-prime numbers, leaving only prime numbers marked as True
