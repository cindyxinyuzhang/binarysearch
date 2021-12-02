class Solution:
    def solve(self, nums):
        return nums[0] < nums[1] and all(nums[i - 1] != nums[i] for i in range(1, len(nums)))
    
    
class Solution:
    def solve(self, nums):
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1] or nums[0] > nums[1]:
                return False
        return True
