# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        temp = head
        l = []
        while(temp):
            if temp not in l:
                l.append(temp)
                temp = temp.next
            else:
                return temp
        return None
