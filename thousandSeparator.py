class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = str(n)
        result = []
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if count == 3:
                result.append(".")
                count = 0
            result.append(s[i])
            count += 1
        return "".join(result[::-1])