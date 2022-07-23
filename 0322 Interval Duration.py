class Solution:
    def solve(self, intervals):
        intervals.sort()

        ans = 0
        last_end = -inf

        for start, end in intervals:
            if start > last_end:
                ans += end - start + 1
            elif end > last_end:
                ans += end - last_end
            
            last_end = max(last_end, end)   

        return ans
