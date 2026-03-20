class Solution(object):
    def sortPeople(self, names, heights):
        combined = list(zip(heights, names))
        combined.sort(key=lambda x: x[0], reverse=True)
        result = [name for height, name in combined]
        
        return result
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        