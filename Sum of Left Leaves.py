# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        total_sum = 0
        if root.left:
            if not root.left.left and not root.left.right:
                total_sum += root.left.val
            else:
                total_sum += self.sumOfLeftLeaves(root.left)
        
        total_sum += self.sumOfLeftLeaves(root.right)
        
        return total_sum