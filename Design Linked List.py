class Node:
    def __init__(self, next=None, val=None):
        self.next = next
        self.val = val

class MyLinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0
        
    def get(self, index: int) -> int:
        if (index >= self.size):
            return -1
        iter = self.head
        for i in range(index):
            iter = iter.next
        return iter.val
            
    def addAtHead(self, val: int) -> None:
        if (self.size == 0):
            self.head.val = val
        else:
            node = Node(next=self.head, val=val)
            self.head = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if (self.size == 0):
            self.addAtHead(val)
        else:
            iter = self.head
            while (iter.next != None):
                iter = iter.next
            iter.next = Node(val=val)
            self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if (index > self.size):
            return
        elif (index == 0):
            self.addAtHead(val)
        elif (index == self.size):
            self.addAtTail(val)
        else:
            iter = self.head
            for i in range(index-1):
                iter = iter.next
            node = Node(next=iter.next, val=val)
            iter.next = node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:   
        if (index >= self.size):
            return
        elif (index == 0):
            self.head = self.head.next
        else:
            iter = self.head
            for i in range(index-1):
                iter = iter.next
            if (index == self.size-1):
                node = iter.next
                iter.next = None
                del node
            else:
                node = iter.next
                iter.next = node.next
                del node
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
