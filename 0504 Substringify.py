class Solution:
    def solve(self, s, t):
        return min(sum(c1!=c2 for c1, c2 in zip(t, s[start:start+len(t)])) for start in range(len(s)-len(t)+1))
