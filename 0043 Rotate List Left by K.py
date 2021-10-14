class Solution:
    def solve(self, nums, k):
        return nums[k:]+nums[:k]
