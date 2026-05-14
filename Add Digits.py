class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        
        # Công thức tính Digital Root (Căn số học)
        return 1 + (num - 1) % 9