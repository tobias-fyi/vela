"""
Python :: Static methods
"""

# %%
class Whatever:
    def __init__(self, num):
        self.num = num
        self.something = self.x_round(num)

    def x_round(self, x):
        if x >= 10:
            return (x ** 4) // 4
        return x


# %%
class Whatever:
    def __init__(self, num):
        self.num = num
        self.something = self.x_round(num)

    @staticmethod
    def x_round(x):
        if x >= 10:
            return (x ** 4) // 4
        return x


# %%
