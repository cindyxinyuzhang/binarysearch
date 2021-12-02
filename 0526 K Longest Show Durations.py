class Solution:
    def solve(self, shows, durations, k):
        time_watched = defaultdict(int)
        for show, duration in zip(shows, durations):
            time_watched[show] += duration
        sorted_time = sorted(list(time_watched.values()), reverse = True)
        return sum(sorted_time[:k])
        
#Time: O(nlogn)
#Space: O(n)
