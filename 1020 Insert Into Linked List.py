# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def solve(self, head, pos, val):
        if not head: return LLNode(val)
        if pos == 0: return LLNode(val, head)

        curr_node = head

        for _ in range(pos-1):
            curr_node = curr_node.next

        curr_node.next = LLNode(val, curr_node.next)

        return head
