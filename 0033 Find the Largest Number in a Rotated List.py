class Solution:
    def solve(self, arr):
        l, r = 0, len(arr)-1
        ans = -inf

        while l <= r:
            m = (l+r)//2
            if arr[m] > arr[-1]:
                l = m+1
                ans = max(ans, arr[m])
            else:
                r = m-1
       
        return max(ans, arr[-1])
