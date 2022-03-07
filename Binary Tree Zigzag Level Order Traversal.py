# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr=[];queue=[(root,0)]
        while queue:
            node,height  = queue.pop(0)
            if height>=len(arr):arr.append(deque())
            if not node: continue
            queue.append((node.left,height+1));queue.append((node.right,height+1))
            if height%2==0:arr[height].append(node.val)
            else:arr[heig
