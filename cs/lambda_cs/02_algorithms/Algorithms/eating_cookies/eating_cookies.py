"""
Algorithms :: Practice - eating cookies

Cookie Monster can eat either 0, 1, 2, or 3 cookies at a time.
If he were given a jar of cookies with `n` cookies inside of it,
how many ways could he eat all `n` cookies in the cookie jar?
Implement a function `eating_cookies` that counts the number of
possible ways Cookie Monster can eat all of the cookies in the jar.
"""

import sys

# n = 6
# [ 1 1 1 1 1 1 ] +1
# [ 1 1 1 1 2 - ] +1
# [ 1 1 2 - 2 - ] +1
# [ 2 - 2 - 2 - ] +1
# [ 1 1 1 3 - - ] +1
# [ 3 - - 3 - - ] +1
# [ 1 2 - 3 - - ] +1

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive recursive solution
def eating_cookies(n: int, cache=None) -> int:
    if cache is None:
        cache = {}
    # cache = {0: 1, 1: 1, 2: 2, 3: 4}
    # Base cases
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    elif cache and cache[n]:
        return cache[n]
    else:
        ec1 = eating_cookies(n - 1, cache)
        ec2 = eating_cookies(n - 2, cache)
        ec3 = eating_cookies(n - 3, cache)
        cache[n] = ec1 + ec2 + ec3

    return cache[n]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print(f"There are {eating_cookies(num_cookies)} ways for")
        print(f"Cookie Monster to eat {num_cookies} cookies.")
    else:
        print("Usage: eating_cookies.py [num_cookies]")

