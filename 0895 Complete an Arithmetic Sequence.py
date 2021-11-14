class Solution:
    def solve(self, nums):
        if len(set(nums)) == 1: return nums[0]

        diff = (nums[-1] - nums[0]) // len(nums)

        expected = []
        for i in range(len(nums)+1) :
            expected.append(nums[0]+i*diff)

        nums_set = set(nums)
        for elem in expected:
            if elem not in nums_set:
                return elem
