"""
Simple Python CLI tool to flatten a directory tree.
I.e. it moves all files under a root directory into that root
(or a diff dir, if specified).
"""

# %%
import argparse
from pathlib import Path
from shutil import move
from typing import List

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
                try:
                    move(str(p), str(dest))
                except:
                    pass
                # Test out by printing path
                # print(p)
            if p.is_dir():  # If dir, add to list of subdirs
                subdirs.append(p)
        # Recursive call on all subdirectories
        flatten_dirs(subdirs, dest)

    return 1


# %%
if __name__ == "__main__":
    # taugo = Path("/Users/Tobias/workshop/taugo")
    # kb = taugo / "kb"
    # sojourn = taugo / "sojourn"
    # flatten_dirs([kb], taugo)

    # Set up the CLI interface
    parser = argparse.ArgumentParser("Flatten Directory Trees")
    parser.add_argument(
        "roots", help="One or more root directories", type=str, nargs="+",
    )
    parser.add_argument(
        "-d",
        "--dest",
        dest="dest",
        type=str,
        nargs=1,
        help="Destination directory for all files under roots. If blank, use current working directory.",
    )
    args = parser.parse_args()

    if args.dest:
        dest = Path(args.dest[0])
    else:
        dest = Path(".")

    # Get the list of directories to flatten into dest, convert to Paths
    roots = [dest / Path(root) for root in args.roots]

    print("Roots:", roots)
    print("Destination:", dest)

    flatten_dirs(roots, dest)


# %%
