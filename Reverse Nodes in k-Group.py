class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def rev(head):
            prev = None
            cur = head
            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev
        
        def revingroups(head,k):
            cur_len = 1
            cur = head
            if not head:return head
            while cur.next and cur_len < k:
                cur = cur.next
                cur_len += 1
            if cur_len < k: return head
            temp_node = cur.next
            cur.next = None
			
            # start linking
            temp_list = revingroups(temp_node,k)
            prev = rev(head)
            head.next = temp_list
            return prev
        return revingroups(head,k)
