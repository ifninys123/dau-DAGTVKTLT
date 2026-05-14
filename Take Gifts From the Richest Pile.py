class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        max_heap = [-g for g in gifts]
        heapq.heapify(max_heap)
        
        for _ in range(k):
            max_val = -heapq.heappop(max_heap)
            heapq.heappush(max_heap, -int(math.floor(math.sqrt(max_val))))
            
        return -sum(max_heap)