# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.order = collections.deque()
        
        def dfs(cur_node):
            if cur_node.left:
                dfs(cur_node.left)
            self.order.append(cur_node.val)
            if cur_node.right:
                dfs(cur_node.right)
        
        dfs(root)
        

    def next(self) -> int:
        return self.order.popleft()

    def hasNext(self) -> bool:
        if self.order:
            return True
        else:
            return False
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
