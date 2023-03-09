# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow = head.next
        fast = head.next.next
        
        while fast and fast.next and slow:
            if fast==slow:
                break
            fast = fast.next.next
            slow = slow.next
        if fast ==slow:
            fast = head
            while fast!=slow:
                fast = fast.next
                slow = slow.next
            return fast
        return None
