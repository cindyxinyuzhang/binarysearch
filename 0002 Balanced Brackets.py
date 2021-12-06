class Solution:
    def solve(self, s):
        balance = 0
        for char in s:
            if char == "(":
                balance += 1
            if char == ")":
                balance -= 1
            if balance < 0:
                return False 
        return balance == 0
