# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if not root: return []

        ans = []
        queue = deque([root])

        while queue:
            for _ in range(len(queue)):
                curr_node = queue.popleft()

                if curr_node.right: queue.append(curr_node.right)
                if curr_node.left: queue.append(curr_node.left)
            
            ans.append(curr_node.val)

        return ans
