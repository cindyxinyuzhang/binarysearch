class Solution:
    def solve(self, nums):
        ans = [0]*len(nums)
        min_num = nums[0]

        for i in range(1, len(nums)):
            ans[i] = min(nums[i-1], min_num)
            min_num = ans[i]
        
        return ans
