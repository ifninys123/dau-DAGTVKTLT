class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        dummy = TreeNode(0)
        self.curr = dummy
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            node.left = None
            self.curr.right = node
            self.curr = node
            
            inorder(node.right)
            
        inorder(root)
        return dummy.right