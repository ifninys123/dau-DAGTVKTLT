class Solution(object):
    def distributeCandies(self, candies, num_people):
        ans = [0] * num_people
        give = 1
        i = 0
        
        while candies > 0:
            idx = i % num_people
            current_gift = min(give, candies)
            
            ans[idx] += current_gift
            candies -= current_gift
            
            give += 1
            i += 1
            
        return ans
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        