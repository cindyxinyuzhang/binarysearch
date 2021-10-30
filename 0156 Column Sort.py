class Solution:
    def solve(self, matrix):
        ans = []

        for nums in zip(*matrix):
            ans.append(sorted([num for num in nums]))  

        return list(zip(*ans))
