class Solution:
    def solve(self, n, friends):
        return len({person for pair in friends for person in pair}) == n
