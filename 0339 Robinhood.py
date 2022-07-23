class Solution:
    def solve(self, n, e, o, t):
        ans = 0
        while n < t:
            growth_rates = [1+e/100, 1+o/100]
            n *= growth_rates[ans%2]
            ans += 1
        return ans
