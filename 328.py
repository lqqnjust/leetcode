# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        o = head 
        e = o.next 
        eh = e 
        while o.next is not None and e.next is not None:
            o.next = e.next 
            o = o.next 
            e.next = o.next 
            e = e.next 

        if o is not None:
            o.next = eh

        return head