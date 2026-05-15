class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = sorted(list(str(num)))
        return (int(digits[0]) * 10 + int(digits[2])) + (int(digits[1]) * 10 + int(digits[3]))