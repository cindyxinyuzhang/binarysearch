class Solution:
    def solve(self, nums):
        return sum(factorial(count)/(2*factorial(count-2)) for count in Counter(nums).values() if count >= 2)
