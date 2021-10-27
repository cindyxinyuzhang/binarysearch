class Solution:
    def solve(self, heights):
        ans = []
        max_height_to_right = 0
        for i in range(len(heights)-1,-1,-1):
            if heights[i] > max_height_to_right:
                ans.append(i)
                max_height_to_right = heights[i]
        return ans[::-1]
      
#Time: O(n)
#Space: O(n)
