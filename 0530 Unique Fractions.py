class Solution:
    def solve(self, fractions):
        ans = set()

        for numerator, denominator in fractions:
            GCD = gcd(numerator, denominator)
            ans.add((numerator//GCD, denominator//GCD))

        return sorted(list(map(list, ans)), key = lambda pair: pair[0]/pair[1])
