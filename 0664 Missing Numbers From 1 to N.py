class Solution:
    def solve(self, nums):
        return sorted(list(set(range(1,len(nums)+1)) - set(nums)))
