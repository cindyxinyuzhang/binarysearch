class Solution:
    def solve(self, nums):
        return 0 if not nums else max(Counter(nums).values())
