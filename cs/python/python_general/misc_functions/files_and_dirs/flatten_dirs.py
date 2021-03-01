"""
Simple Python script to flatten a directory tree.
I.e. it moves all files under a root directory into that root
(or a diff dir, if specified).
"""

# %%
from collections import deque
from pathlib import Path
from shutil import move
from typing import List

# %%
def flatten(roots: List[Path], dest: Path, stack: deque = None) -> int:
    """Move all files under directories in `root` to the dest directory.
    I.e. recursive (depth-first) traversal that moves each leaf into another directory.

    :param roots (List[str]) : List of directories to flatten into dest.
    :param dest (str) : Destination directory for all files under roots.
    :return (int) : Returns 1 upon successful completion.
    """
    # Create a new stack object to store the paths
    if stack is None:
        stack = deque()
    # Add roots onto (right side of) stack
    stack.extend(roots)
    # Base Case: no subdirectories of current dir (list of roots is empty)
    try:
        cur_dir = stack.pop()  # Pop a path from the stack
    except IndexError:  # return / back out of the call stack
        return
    # Recursive Case: subdirectories exist (stack is not empty)
    for path in cur_dir.iterdir():
        if path.is_dir():  # Add all immediate subdirectories to stack
            stack.append(path)
        if path.is_file():  # Move all files in current dir to dest
            move(path, dest)

    return 1


# %%
def flatten_dirs(roots: List[Path], dest: Path) -> int:
    """Move all files under directories in `root` to the dest directory.
    I.e. recursive (depth-first) traversal that moves each leaf into another directory.

    :param roots (List[str]) : List of directories to flatten into dest.
    :param dest (str) : Destination directory for all files under roots.
    :return (int) : Returns 1 upon successful completion.
    """
    if len(roots) == 0:  # Base case: no subdirectories to traverse
        return
    # Recursive case
    # Loop through roots, recursively calling the func on those dirs
    for root in roots:
        subdirs = []
        for p in root.iterdir():  # Loop through child paths
            if p.is_file():  # If file, move
                # move(p, dest)
                # Test out by printing path
                print(p)
            if p.is_dir():  # If dir, add to list of subdirs
                subdirs.append(p)
        # Recursive call on all subdirectories
        flatten_dirs(subdirs, dest)

    return 1


# %%
taugo = Path("/Users/Tobias/workshop/taugo")
kb = taugo / "kb"
sojourn = taugo / "sojourn"


# %%
flatten_dirs([kb], taugo)

# %%
