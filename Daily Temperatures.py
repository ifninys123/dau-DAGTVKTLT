class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        answer = [0] * n
        stack = []  # Lưu cặp (index, temperature) hoặc chỉ cần index
        
        for i in range(n):
            current_temp = temperatures[i]
            # Khi tìm thấy ngày ấm hơn ngày ở đỉnh stack
            while stack and temperatures[stack[-1]] < current_temp:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            stack.append(i)
            
        return answer