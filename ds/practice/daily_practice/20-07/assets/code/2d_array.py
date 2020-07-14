"""
HackerRank :: 2D Array
"""

# === Array for testing === #
arr = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0],
]

# One option is to define a class with methods to move the hourglass
class Hourglass:
    def __init__(self):
        x1 = [0, 1, 2]
        x2 = [1]
        x3 = [0, 1, 2]


# Complete the hourglassSum function below.
def hourglassSum(arr):
    pass


# === Version 1 === #
# Set up hourglass / "window" index structure
# [0][:3]
# [1][1]
# [2][:3]
# Calculate the sum of the hourglass values, insert into separate array
# Iterate to move the hourglass "window" by 1 along horizontal axis
# Once hourglass edge hits the other edge, move to next index on vertical axis
# Iterate until all 16 sums

# Could use a single while loop and if statements that increment two pointers,
# one for each axis

x = 3
y = 3

# To keep full hourglass in array, ...
# Horizontal: loop through range of indexes 3 - len(arr[0])
# Vertical: loop through range of indexes 3 - len(arr)
while x < len(arr[0]) and y < len(arr):
    row1 = arr[y - 3][x - 3 : x]
    row2 = arr[y - 2][x - 2]
    row3 = arr[y - 1][x - 3 : x]
