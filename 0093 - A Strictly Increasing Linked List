# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, head):
        curr = head
        while curr.next:
            if curr.val >= curr.next.val:
                return False
            curr = curr.next
        return True
        
#Time: O(n)
#Space: O(1)
