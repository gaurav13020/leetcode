# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        left = head
        right = self.middleNode(head)
        temp = right.next
        right.next = None
        right = temp
        left = self.sortList(left)
        right = self.sortList(right)
        return self.mergeTwoLists(left, right)
    
    def middleNode(self, head: Optional[ListNode]):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        tail = head = ListNode()
    
        while list1 and list2: #same as list1 != None and list2 != None
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
                
            else:
                tail.next = list2
                list2 = list2.next
                
            tail = tail.next
        while list1:
            tail.next = list1
            list1 = list1.next
            tail = tail.next
            
        while list2:
            tail.next = list2
            list2 = list2.next
            tail = tail.next
            
        return head.next