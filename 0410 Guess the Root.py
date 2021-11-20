class Solution:
    def solve(self, n):
        l, r = 0, ceil(n/2)
        ans = -1
        while l <= r:
            m = (l+r)//2
            if m**2 <= n:
                ans = m
                l = m+1
            else:
                r = m-1
        return ans
    
    #bs on the answer
