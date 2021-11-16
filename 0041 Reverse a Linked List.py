# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        if not node: return None

        prev, curr = None, node

        while curr:
            original_next = curr.next
            curr.next = prev
            prev, curr = curr, original_next

        return prev
