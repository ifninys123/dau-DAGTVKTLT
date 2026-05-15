class Solution(object):
    def checkValid(self, matrix):
        m = len(matrix)
        for i in matrix:
            if len(set(i)) != m:
                return False
        for i in zip(*matrix):
            if len(set(i)) != m:
                return False
        return True
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        