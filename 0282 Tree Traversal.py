# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, moves):
        new_moves = []

        for move in moves:
            if move == 'UP':
                new_moves.pop()
            else:
                new_moves.append(move)

        node = root
        for move in new_moves:
            if move == 'RIGHT':
                node = node.right
            else:
                node = node.left

        return node.val
