class Solution(object):
    def findMode(self, root):
        self.prev = None
        self.count = 0
        self.max_count = 0
        self.result = []

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            if self.prev is not None and node.val == self.prev:
                self.count += 1
            else:
                self.count = 1
            
            if self.count > self.max_count:
                self.max_count = self.count
                self.result = [node.val]
            elif self.count == self.max_count:
                self.result.append(node.val)
            
            self.prev = node.val
            
            inorder(node.right)

        inorder(root)
        return self.result