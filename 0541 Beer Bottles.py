class Solution:
    def solve(self, n):
        empty, drunken = n, n
        while empty >= 3:
            new = empty // 3
            empty %= 3
            empty += new
            drunken += new
        return drunken
