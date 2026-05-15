class Solution(object):
    def areOccurrencesEqual(self, s):
        char_counts = {}
        for char in s:
            char_counts[char] = char_counts.get(char, 0) + 1
            frequencies = set(char_counts.values())
        return len(frequencies) == 1
        """
        :type s: str
        :rtype: bool
        """
        