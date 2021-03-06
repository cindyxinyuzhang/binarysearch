class Solution:
    def solve(self, n):
        counter = 0
        while n != 1:
            if not n%2: n = n / 2
            else: n = 3 * n + 1
            counter += 1
        return counter+1 #while loop exists when n = 1, so the counter needs to add 1
        
#space: O(1)
