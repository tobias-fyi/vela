"""Basic unit tests for recursive hex-decimal converter"""

# %%
import pytest

from hex_convert_rec import *

# %%
hex_in = "#7D3545"


def test_hex2dec():
    assert hex2dec(hex_in) == False


# %%
