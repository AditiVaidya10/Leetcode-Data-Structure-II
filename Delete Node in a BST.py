# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if root.val == key:
            if not (root.right or root.left):
                del root
                return None
            
            elif root.left and not root.right:
                return root.left
            
            elif not root.left and root.right:
                return root.right
           
            else:
                NewRoot = cur = root.right
                while cur.left:
                    cur = cur.left
                cur.left = root.left
                
                return NewRoot
            
        if root.val > key: 
            root.left = self.deleteNode(root.left,key)  
        if root.val < key: 
            root.right = self.deleteNode(root.right,key) 
        return root
