# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if not root: return True

        queue = deque([root])

        while queue:
            curr_node = queue.popleft()

            left = curr_node.left.val if curr_node.left else 0
            right = curr_node.right.val if curr_node.right else 0

            if left + right != curr_node.val and (curr_node.left or curr_node.right):
                return False
            
            if curr_node.left: queue.append(curr_node.left)
            if curr_node.right: queue.append(curr_node.right)

        return True
