
class Solution:
    def solve(self, nums):
        if len(nums) < 2: return False
        max1, max2 = -inf, -inf
        for num in nums:
            if num >= max1: max1, max2 = num, max1
            elif num > max2: max2 = num
        return max1 > 2*max2

#time: O(n)
#space: O(1)



class Solution:
    def solve(self, nums):
        return sorted(nums)[-1] > (sorted(nums)[-2]*2)

#time: O(nlogn)
#space: O(n)
