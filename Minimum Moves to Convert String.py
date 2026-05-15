class Solution(object):
    def minimumMoves(self, s):
        """
        :type s: str
        :rtype: int
        """
        moves = 0
        i = 0
        n = len(s)
        
        while i < n:
            # Nếu gặp 'X', ta buộc phải thực hiện một bước nhảy 3 ô
            if s[i] == 'X':
                moves += 1
                i += 3  # Nhảy qua 3 ký tự vì 1 move xử lý được cụm 3
            else:
                # Nếu là 'O', chỉ cần tiến lên 1 bước để tìm chữ 'X' tiếp theo
                i += 1
                
        return moves