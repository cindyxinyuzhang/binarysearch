# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if not root: return 0
        return self.solve(root.left) + self.solve(root.right) + root.val
    
# ^ recursive solution


# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if not root: return 0
        ans = 0
        queue = deque([root])
        while queue:
            curr_node = queue.popleft()
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
            ans += curr_node.val
        return ans
    
# ^ iterative solution bfs
