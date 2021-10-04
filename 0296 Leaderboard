class Solution:
    def solve(self, nums):
        rank_dict = {}
        for rank,score in enumerate(sorted(list(set(nums)), reverse = True)):
            rank_dict[score] = rank
        return [rank_dict[num] for num in nums]
