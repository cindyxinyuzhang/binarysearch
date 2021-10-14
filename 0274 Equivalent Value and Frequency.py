class Solution:
    def solve(self, nums):
        return any(key == val for key, val in Counter(nums).items())
