# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        pre = dummy
        cur = head 
        while cur and cur.next:
            next_node = cur.next.next #3
            pre.next  = cur.next # 0-2
            cur.next.next = cur # 2-1
            cur.next = next_node # 1-3
            pre = cur # 1
            cur = next_node # 3
        return dummy.next