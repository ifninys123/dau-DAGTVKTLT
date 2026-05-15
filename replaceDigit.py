class Solution(object):
    def replaceDigits(self, s):
        s_list = list(s)
        for i in range(1, len(s_list), 2):
            char_before = s_list[i-1]
            shift_val = int(s_list[i])
            s_list[i] = chr(ord(char_before) + shift_val)
        return "".join(s_list)
        """
        :type s: str
        :rtype: str
        """
        