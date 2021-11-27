# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        prev, curr = None, node
        while curr:
            try:
                prev = curr
                for _ in range(curr.val):
                    curr = curr.next
                prev.next = curr
            except:
                prev.next = None
                return node
        return node
