class Solution:
    def solve(self, nums):
        if not nums: return []

        c = Counter(nums)
        seen = set()
        ans = []

        for num in nums:
            if num not in seen:
                seen.add(num)
                ans.append(num)
            elif c[num] > 2:
                c[num] -= 1
                ans.append(num)

        return ans

    
class Solution:
    def solve(self, nums):
        if not nums: return []

        c = Counter(nums)
        removed = set()

        for i in range(len(nums)-1, -1, -1):
            num = nums[i]

            if c[num] > 1 and num not in removed:
                nums.pop(i)
                removed.add(num)

        return nums    
