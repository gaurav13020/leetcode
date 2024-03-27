# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        temp = head
        length = 0
        while temp:
            temp = temp.next
            length += 1
    
    
        dummy = ListNode(0, head)
        prev = dummy
        cur = head
        for i in range(length - n):
            prev = prev.next
            cur = cur.next
        prev.next = cur.next
        return dummy.next
        