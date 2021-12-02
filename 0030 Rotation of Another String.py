class Solution:
    def solve(self, s0, s1):
        return s0 in s1*2 and len(s0) == len(s1)

#time: O(n*m) string in string checking
#space: O(m)
