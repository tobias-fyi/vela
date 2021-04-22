"""Recursive hex code conversion functions"""

# %%
hex_color_in = "#7D3545"

# int(0xF6A) -> 3,946
hex_in = "F6A"


def hex2dec(hex: str) -> int:
    # Clean/strip and validate input
    # Pop first letter from string and convert to dec
    # Calculate current value of dec: 16**lenth(string) - 1
    # Base Case: no characters left in string
    # Return None (?)
    # Recursive case
    # Return current value + recursive call on leftover
    pass


hex2dec(hex_in)

