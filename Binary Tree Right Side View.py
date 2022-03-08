# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        stack = [root]
        result = [root.val]
        while stack:
            answers = []
            inner_stack = []
            for i in range(0,len(stack)):
                node = stack[i]
                if node.left :
                    inner_stack.append(node.left)
                    answers.append(node.left.val)
                if node.right:
                    inner_stack.append(node.right)
                    answers.append(node.right.val)
            stack = inner_stack
            if len(answers) > 0:
                result.append(answers[-1])
        return result
