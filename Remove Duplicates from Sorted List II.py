# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        itr=head
        while itr:
            itr=itr.next
      
        d={}
        itr=head
        while itr:
            if itr.val not in d:
                d[itr.val]=0
            d[itr.val]+=1
            itr=itr.next
        node=ListNode(0,None)
        temp=node
        for i,j in d.items():
            if j==1:
                curr=ListNode(i,None)
                node.next=curr
                node=node.next
        return temp.next
