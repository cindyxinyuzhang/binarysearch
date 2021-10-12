class Solution:
    def solve(self, nums):
        reverse = nums[::-1]
        sort = sorted(nums)
        reverse_sort = sort[::-1]

        if not nums or nums == sort: return 0

        for i in range(len(nums)):
            if nums[i] != sort[i]:
                first = i
                break
        for i in range(len(nums)):
            if reverse[i] != reverse_sort[i]:
                last = len(nums)-i
                break
        return last - first
