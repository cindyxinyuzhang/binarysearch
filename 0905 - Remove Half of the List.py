class Solution:
    def solve(self, nums):
        target_len = len(nums)//2
        curr_len = len(nums)
        ans = 0

        for count in sorted(Counter(nums).values(), reverse = True):
            curr_len -= count
            ans += 1
            if curr_len <= target_len:
                return ans
