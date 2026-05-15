class Solution(object):
    def capitalizeTitle(self, title):
        w = title.split()
        proc_word = [word.lower() if len(word)<=2 else word.title() for word in w]
        return " ".join(proc_word)
        """
        :type title: str
        :rtype: str
        """
        