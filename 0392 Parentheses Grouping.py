class Solution:
    def solve(self, s):
        stack = 0
        ans = []
        l = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack += 1
            else:
                stack -= 1
            if stack == 0:
                ans.append(s[l:i+1])
                l = i+1
        return ans
