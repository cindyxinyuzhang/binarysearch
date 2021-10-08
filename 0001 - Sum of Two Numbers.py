class Solution:
    def solve(self, nums, k):
        nums.sort()
        l, r = 0, len(nums)-1
        while l < r:
            if nums[l]+nums[r] > k: r -= 1
            elif nums[l]+nums[r] < k: l += 1
            else: return True
        return False
        
        
#Time: O(nlogn) sorting


class Solution:
    def solve(self, nums, k):
        s = set()
        for num in nums:
            if k-num in s: return True
            s.add(num)
        return False
        
#Time: O(n)
#Space: O(1)
