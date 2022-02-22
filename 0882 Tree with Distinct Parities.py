# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if not root: return 0

        ans = 0

        def subtree_sum(node):
            if not node: return 0

            nonlocal ans

            left = subtree_sum(node.left)
            right = subtree_sum(node.right)

            if node.left and node.right and (left+right)%2==1:
                ans += 1

            return node.val + left + right
        
        subtree_sum(root)

        return ans
