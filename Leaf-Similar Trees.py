class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def get_leaves(root):
            leaves = []
            stack = [root]
            while stack:
                node = stack.pop()
                if not node.left and not node.right:
                    leaves.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            return leaves
        
        return get_leaves(root1) == get_leaves(root2)