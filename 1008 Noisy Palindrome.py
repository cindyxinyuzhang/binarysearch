class Solution:
    def solve(self, s):
        stripped = ''.join(char for char in s if char.islower())
        return stripped == stripped[::-1]
