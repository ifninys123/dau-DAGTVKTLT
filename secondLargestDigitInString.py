class Solution(object):
    def secondHighest(self, s):
        first = second = -1
        
        for char in s:
            if char.isdigit():
                val = int(char)
                if val > first:
                    second = first
                    first = val
                elif second < val < first:
                    second = val
                    
        return second
    """
    :type s: str
    :rtype: int
    """
        