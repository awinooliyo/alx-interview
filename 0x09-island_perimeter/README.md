# Island Perimeter Calculator

## Project Overview
This project is designed to calculate the perimeter of an island represented in a 2D grid. The grid consists of land (`1`) and water (`0`) cells, and the task is to determine the total perimeter of the island by evaluating its boundary cells.

## Features
- The function `island_perimeter(grid)` calculates the perimeter of the island.
- The grid is represented by a 2D list of integers where:
  - `0` represents water.
  - `1` represents land.
- Cells are square with side length of 1.
- Cells are connected horizontally or vertically (not diagonally).
- The perimeter is determined by counting the number of edges that touch water or are on the grid boundary.

## Files
- **0-island_perimeter.py**: Contains the function `island_perimeter(grid)` that calculates the perimeter.
- **0-main.py**: A test script to run the function with a sample grid.

## Requirements
- All files are to be interpreted and compiled on Ubuntu 20.04 LTS using Python 3.
- PEP 8 style guide (version 1.7) should be followed for the Python code.
- The grid is rectangular with width and height not exceeding 100.
- There is only one island in the grid, and no internal "lakes" (water inside the island not connected to the surrounding water).
- No external modules are to be imported.

## Function Description

```python
def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list of list of int): 2D array where 1 represents land and 0 represents water.

    Returns:
        int: The perimeter of the island.
    """
