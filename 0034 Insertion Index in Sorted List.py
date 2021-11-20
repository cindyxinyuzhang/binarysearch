class Solution:
    def solve(self, nums, target):
        l, r = 0, len(nums)
        ans = -1
        while l <= r:
            m = (l+r)//2
            if m == len(nums) or nums[m] > target:
                ans = m
                r = m-1
            else:
                l = m+1
        return ans
