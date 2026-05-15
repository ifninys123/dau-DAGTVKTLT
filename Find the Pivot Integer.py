class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        total_sum = n * (n + 1) // 2
        x = math.sqrt(total_sum)
        if x % 1 == 0:
            return int(x)
        
        return -1