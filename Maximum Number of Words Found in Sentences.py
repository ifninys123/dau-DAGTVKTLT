class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max_words = 0
        for sentence in sentences:
            word_count = sentence.count(' ') + 1
            if word_count > max_words:
                max_words = word_count
        return max_words