class Solution:
    def solve(self, s, k):
        return len(set(s))**ceil(k/2)
