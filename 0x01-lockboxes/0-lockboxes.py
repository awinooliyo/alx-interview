#!/usr/bin/python3
"""
Module: lockboxes

Contains the function canUnlockAll to determine if all lockboxes can be opened.
"""

def canUnlockAll(boxes):
    """
    Determines if all lockboxes can be opened starting from the first box.

    Args:
    - boxes (list of list of int): List of lockboxes where each box (index) contains a list of keys (integers).

    Returns:
    - bool: True if all lockboxes can be opened, False otherwise.

    Assumptions:
    - The first box (boxes[0]) is always unlocked.
    - Keys are positive integers that correspond to indices of other boxes.
    - Some keys may not have corresponding boxes.
    """
    n = len(boxes)
    if n == 0:
        return False
    
    visited = set()
    visited.add(0)  # Start from the first box which is unlocked
    queue = [0]     # Queue to manage boxes to be opened next
    
    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < n and key not in visited:
                visited.add(key)
                queue.append(key)
    
    return len(visited) == n

