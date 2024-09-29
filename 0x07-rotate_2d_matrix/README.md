# 2D Matrix Rotation - 90 Degrees Clockwise

## Problem Description

This program rotates an `n x n` 2D matrix 90 degrees clockwise **in place** without using any extra space for another matrix.

### Example

Given the matrix:

```python
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
The matrix after rotating 90 degrees clockwise will be:
```python
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]

How the Solution Works
The solution to rotate a 2D matrix 90 degrees clockwise involves two primary steps:

Reverse the matrix: Reverse the order of rows in the matrix.
Transpose the matrix: Swap elements across the main diagonal (i.e., swap matrix[i][j] with matrix[j][i] where i > j).

First, we reverse the order of the rows in the matrix. For example, consider the original matrix:
```bash
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
After reversing the rows, the matrix looks like this:
```[
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3]
]

We then transpose the matrix:
Next, we swap the elements along the diagonal of the matrix. Specifically, we swap matrix[i][j] with matrix[j][i] for all elements where i > j. This effectively transposes the matrix, transforming rows into columns.

Here’s how the transposition works step by step:

Swap matrix[1][0] with matrix[0][1]. The elements 4 and 8 are swapped.
Swap matrix[2][0] with matrix[0][2]. The elements 1 and 9 are swapped.
Swap matrix[2][1] with matrix[1][2]. The elements 2 and 6 are swapped.
After performing these swaps, the matrix becomes:
```bash
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
