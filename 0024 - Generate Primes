class Solution:
    def solve(self, n):
        if n < 2: return []
        ans = []
        for num in range(2,n+1):
            if all(num%i!=0 for i in range(2,num)): ans.append(num)
        return ans
