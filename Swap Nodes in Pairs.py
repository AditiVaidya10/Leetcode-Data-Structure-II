# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        prev=dummy
        current=head
        dummy.next=head
        while current!=None and current.next!=None:
            prev.next=current.next
            current.next=current.next.next
            prev.next.next=current
            current=current.next
            prev=prev.next.next
        return dummy.next
