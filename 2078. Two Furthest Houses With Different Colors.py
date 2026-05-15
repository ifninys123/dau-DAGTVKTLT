class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        n = len(colors)
        max_dist = 0
        
        for i in range(n):
            if colors[i] != colors[0]:
                max_dist = max(max_dist, i)
            if colors[i] != colors[n - 1]:
                max_dist = max(max_dist, n - 1 - i)
                
        return max_dist