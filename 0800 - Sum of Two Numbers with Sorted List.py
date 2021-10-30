class Solution:
    def solve(self, nums, k):
        if len(nums) < 2: return False

        l, r = 0, len(nums)-1

        while l < r:
            elem_sum = nums[l] + nums[r]
            if elem_sum == k:
                return True
            elif elem_sum > k:
                r -= 1
            else:
                l += 1

        return False
