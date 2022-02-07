class Solution:
    def solve(self, nums):
        if len(nums) < 2: return 0
        if len(nums) == 2: return nums[0]*nums[1]
        
        max1, max2 = 0, 0
        min1, min2 = 0, 0

        for num in nums:
            if num > max2:
                if num >= max1:
                    max1, max2 = num, max1
                else:
                    max2 = num
            elif num < min2:
                if num <= min1:
                     min1, min2 = num, min1
                else:
                    min2 = num                   

        return max(max1*max2, min1*min2)
