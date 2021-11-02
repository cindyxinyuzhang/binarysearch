class Solution:
    def solve(self, nums):
        nums_set = set(nums)
        return sum(num+1 in nums_set for num in nums)
