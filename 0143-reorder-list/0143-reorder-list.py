# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = slow.next = None
        
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
            
        f, s = head, prev
        while s:
            temp1, temp2 = f.next, s.next
            f.next = s
            s.next = temp1
            f = temp1
            s = temp2