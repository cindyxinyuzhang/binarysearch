# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, lo, hi):
        if not root: return 0

        root_val = 1 if lo <= root.val <= hi else 0

        return self.solve(root.left, lo, hi) + self.solve(root.right, lo, hi) + root_val
