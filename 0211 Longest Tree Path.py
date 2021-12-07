# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        self.ans = 0
        self.longest_upward_path(root)

        return self.ans

    def longest_upward_path(self, node):
        if not node: return 0
        left = self.longest_upward_path(node.left)
        right = self.longest_upward_path(node.right)
        self.ans = max(self.ans, left + right + 1)
        return max(left, right) + 1
