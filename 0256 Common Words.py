class Solution:
    def solve(self, s0, s1):
        return len(set(s0.lower().split()) & set(s1.lower().split() ))
