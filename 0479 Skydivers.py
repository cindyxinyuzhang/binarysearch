class Solution:
    def solve(self, nums, k):

        def works(capacity):
            days = 1
            curr_capacity = capacity
            for num in nums:
                if num > curr_capacity:
                    days += 1
                    curr_capacity = capacity
                curr_capacity -= num
            return days <= k
            
        ans = inf
        l, r = max(nums), sum(nums)
        while l <= r:
            m = (l+r)//2
            if works(m):
                r = m-1
                ans = min(ans, m)
            else:
                l = m+1
        return ans
