class Solution:
    def solve(self, intervals):
        if not intervals: return 0
        
        intervals.sort()
        res = 0
        prev_end = intervals[0][1]

        for interval in intervals[1:]:
            if interval[0] >= prev_end:
                prev_end = interval[1]
            else:
                res += 1
                prev_end = min(prev_end, interval[1])
        return res
     
#Time: O(nlogn)
#Space: O(n)  .sort() uses Timsort and takes worst case O(n) space
