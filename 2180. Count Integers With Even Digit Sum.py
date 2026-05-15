class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        temp = num
        digit_sum = 0
        while temp > 0:
            digit_sum += temp % 10
            temp //= 10
            
        if digit_sum % 2 == 0:
            return num // 2
        else:
            return (num - 1) // 2