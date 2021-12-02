class Solution:
    def solve(self, words):
        if not words: return 0

        streak = 1
        ans = 1

        for i in range(1,len(words)):
            if words[i][0] == words[i-1][0]: streak += 1
            else: streak = 1
            ans = max(ans, streak)

        return ans
