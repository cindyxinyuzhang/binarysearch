class Solution:
    def solve(self, matrix):
        return list(zip(*matrix[::-1]))[::-1]
