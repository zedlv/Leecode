# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        pre = dummy
        cur = head 
        while n:
            cur = cur.next
            n -= 1
        while cur:
            pre = pre.next
            cur = cur.next
        pre.next = pre.next.next
        return dummy.next