# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#【热题100】02-合并两个有效的链表
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        if list1.val<list2.val:
            list1.next = self.mergeTwoLists(list1.next,list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list2.next,list1)
            return list2

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 虚拟头节点（简化边界处理，无需单独判断头节点）
        dummy = ListNode(val=-1)
        # 游标指针：用于构建合并后的链表
        cur = dummy
        
        # 遍历两个链表，直到其中一个为空
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1  # 指向较小的节点
                list1 = list1.next # list1指针后移
            else:
                cur.next = list2  # 指向较小的节点
                list2 = list2.next # list2指针后移
            cur = cur.next  # 游标指针后移
        
        # 处理剩余节点（其中一个链表已空，直接拼接另一个）
        cur.next = list1 if list1 else list2
        
        # 返回虚拟头节点的next（合并后链表的真正头节点）
        return dummy.next