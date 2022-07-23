class Solution:
    def solve(self, intervals):
        intervals.sort()
        ans = 0
        streak = 0
        last_end = -inf

        for start, end in intervals:
            if start > last_end: # seperate interval
                ans = max(ans, streak)
                streak = end-start+1
            elif end > last_end: # overlapping 
                streak += end-last_end

            last_end = max(last_end, end)

        return max(ans, streak) # in case the last streak is larger than ans
