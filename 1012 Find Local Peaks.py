class Solution:
    def solve(self, nums):
        n, ans = len(nums), []

        if n == 1: return []
        
        if nums[0] > nums[1]:
                ans.append(0)
        if nums[n-2] < nums[-1]:
                ans.append(n-1)
        for i in range(1, n-1):
            if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                ans.append(i)
        return sorted(ans)
