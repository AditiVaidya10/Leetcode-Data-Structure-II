class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if k == 1:
            return n
        head = Node(1)
        cur = head
        for i in range(2, n + 1):
            cur.next = Node(i)
            cur = cur.next
        cur.next = head
        count = 1
        while head != head.next:
            if k - count == 1:
                count = 1
                head.next = head.next.next
            else:
                count += 1
            head = head.next
        return head.val
