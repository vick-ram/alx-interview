#!/usr/bin/python3
"""0-island_perimeter module"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in the grid"""
    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if (
                        new_row < 0
                        or new_row >= rows
                        or new_col < 0
                        or new_col >= cols
                        or grid[new_row][new_col] == 0
                    ):
                        perimeter += 1

    return perimeter