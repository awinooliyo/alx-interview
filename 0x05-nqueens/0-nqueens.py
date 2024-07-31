#!/usr/bin/python3

"""
N Queens Solver (Python)

This script solves the N Queens problem using a backtracking
approach. It places N non-attacking queens on an N×N chessboard
and prints all possible solutions.

Usage:
    ./0-nqueens.py N

Arguments:
    N: An integer greater than or equal to 4 representing the size
       of the chessboard.
"""

import sys
from typing import List


def print_usage_and_exit() -> None:
    """
    Prints the usage message and exits the program with status 1.
    """
    print("Usage: nqueens N")
    sys.exit(1)


def validate_n(n: str) -> int:
    """
    Validates the input number N.

    Args:
        n (str): The input number as a string.

    Returns:
        int: The validated number.

    Raises:
        SystemExit: If N is not an integer or is less than 4.
    """
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(n)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_valid(board: List[int], row: int, col: int) -> bool:
    """
    Checks if placing a queen at (row, col) is valid.

    Args:
        board (List[int]): The current state of the board.
        row (int): The row where the queen is to be placed.
        col (int): The column where the queen is to be placed.

    Returns:
        bool: True if the position is valid, False otherwise.
    """
    for i in range(row):
        if (board[i] == col or
                board[i] - i == col - row or
                board[i] + i == col + row):
            return False
    return True


def solve_nqueens(n: int, board: List[int], row: int) -> None:
    """
    Solves the N Queens problem using backtracking.

    Args:
        n (int): The size of the chessboard.
        board (List[int]): The current state of the board.
        row (int): The current row being processed.
    """
    if row == n:
        solutions.append([[i, board[i]] for i in range(n)])
        return

    for col in range(n):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens(n, board, row + 1)
            board[row] = -1


def main() -> None:
    """
    Main function to handle input and start solving the N Queens
    problem.
    """
    if len(sys.argv) != 2:
        print_usage_and_exit()

    n = sys.argv[1]
    n = validate_n(n)

    global solutions
    solutions = []

    board = [-1] * n
    solve_nqueens(n, board, 0)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
