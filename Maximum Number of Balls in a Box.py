class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        boxes = {}
        
        for ball in range(lowLimit, highLimit + 1):
            digit_sum = 0
            temp = ball
            while temp > 0:
                digit_sum += temp % 10
                temp //= 10
            
            boxes[digit_sum] = boxes.get(digit_sum, 0) + 1
            
        return max(boxes.values())