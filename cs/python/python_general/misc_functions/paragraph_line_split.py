"""Sprint up a long string into multiple lines."""

# %% imports
from typing import List

# %%
def split_into_lines(s: str, line_hgt: int = 14, width: int = 100,) -> List[str]:
    lines = []  # List of lines to return
    line = ""  # Current line's string
    for word in s.split():  # Loop through words
        if len(line) + len(word) < 100:
            line += " " + word  # add each one to the current line's string
        # If the next word would cause the string to be wider than the width...
        else:  # ..."write" / reset the line
            # c.drawString(x, y - (len(lines) * line_hgt), line)
            lines.append(line.strip())
            line = word  # Start new line with current word
    lines.append(line)  # Add last line before returning all lines
    return lines


# %%
thistring = "Do a good job — not just any good job, but a great job. I am a smart person and I need a great product. And this here should be on a new line! Here's some more and more, just trying to fill that empty space, like any good and decent human-type of humanoid should do."
split_into_lines(thistring)

# %% Recursive solution
def split_lines_recursively():
    # TODO: solve with recursion
    pass


# %% Generator solution
def split_line_generator():
    # TODO: solve with generators
    pass

