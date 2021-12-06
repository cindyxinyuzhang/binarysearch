class Solution:
    def solve(self, s, k):
        return (2*k-1)*'.' in s or s.startswith(k*'.') or s.endswith(k*'.')
