# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans=[]
        def dfs(root,s,curr):
            if root is None:
                return False
            s=s+root.val
            if s==targetSum and root.left is None and root.right is None:
                curr.append(root.val)
                ans.append(curr)
                return 
            left=dfs(root.left,s,curr+[root.val])
            right=dfs(root.right,s,curr+[root.val])
            
        dfs(root,0,[])
        return ans
