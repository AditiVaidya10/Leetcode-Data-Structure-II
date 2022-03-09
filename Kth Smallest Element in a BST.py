# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return root
        arr = []
        self.inorder_traversal_recursively(root,arr)
        if k > len(arr) or k <=0:
            return None
        else:
            return arr[k-1]
    
    def inorder_traversal_recursively(self, root, arr):
        if root:
            self.inorder_traversal_recursively(root.left,arr)
            arr.append(root.val)
            self.inorder_traversal_recursively(root.right,arr)
