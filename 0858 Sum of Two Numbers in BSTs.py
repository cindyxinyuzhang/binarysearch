# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, a, b, target):

        def dfs(root):
            if not root: return set()

            vals = set()
            stack = [root]
            
            while stack:
                node = stack.pop()
                vals.add(node.val)
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)

            return vals

        vals_a, vals_b = dfs(a), dfs(b)

        for val in vals_a:
            if target - val in vals_b:
                return True
                
        return False
