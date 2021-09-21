class Solution:
    def solve(self, s):
        pos = 0
        q_counter = 0
        for char in s:
            if char == 'L': 
                pos -= 1
            elif char == 'R': 
                pos += 1
            else: 
                q_counter += 1
        return abs(pos + q_counter) if pos > 0 else abs(pos - q_counter)
       
#Time: O(n)
#Space: O(1)
