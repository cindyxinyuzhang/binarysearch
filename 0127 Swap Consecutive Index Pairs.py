class Solution:
    def solve(self, nums):
        for i in range(0,l:=len(nums),4):
            if i+2<l: 
                nums[i], nums[i+2] = nums[i+2], nums[i]
            if i+3<l: 
                nums[i+1], nums[i+3] = nums[i+3], nums[i+1]
        return nums
