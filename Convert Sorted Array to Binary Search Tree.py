# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if nums : 
            point = len(nums)//2
            tree = TreeNode(nums[point])
            if nums[:point] :
                tree.left = self.sortedArrayToBST(nums[:point])
            if nums[point:] :
                tree.right = self.sortedArrayToBST(nums[point+1:])
            return tree
