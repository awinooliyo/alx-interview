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
