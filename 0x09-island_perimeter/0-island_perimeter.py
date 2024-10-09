#!/usr/bin/python3
"""
Function to calculate the perimeter of the island
"""

def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.
    
    Args:
        grid (list of list of int): 2D array where 1 represents land and 0 represents water.
    
    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Check all four possible sides (up, down, left, right)
                # Add to perimeter if the side is either water or out of bounds
                if r == 0 or grid[r-1][c] == 0:  # Check above
                    perimeter += 1
                if r == rows - 1 or grid[r+1][c] == 0:  # Check below
                    perimeter += 1
                if c == 0 or grid[r][c-1] == 0:  # Check left
                    perimeter += 1
                if c == cols - 1 or grid[r][c+1] == 0:  # Check right
                    perimeter += 1
    
    return perimeter
