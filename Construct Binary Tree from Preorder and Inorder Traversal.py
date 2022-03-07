# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hash_map = {}
        for i in range(len(inorder)):
            hash_map[inorder[i]] = i
        
        def helper(preorder, pstart, pend, inorder, istart, iend):
            
            
            if pstart > pend:
                return None
            elif pstart == pend:
                return TreeNode(preorder[pstart])
            
            root = TreeNode(preorder[pstart])
            
            rootindex = hash_map[preorder[pstart]]
            
            numleft = rootindex - istart
            
            root.left = helper(preorder, pstart+1, pstart + numleft, inorder, istart,rootindex-1 )
            root.right = helper(preorder, pstart + numleft +1, pend, inorder, rootindex +1, iend)
            
            return root
            
        return (helper(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1))
