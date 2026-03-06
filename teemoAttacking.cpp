class Solution {
public:
    int findPoisonedDuration(vector<int>& timeSeries, int duration) {
        int n = timeSeries.size();
    if (n == 0) return 0;
    
    int totalDuration = 0;
    
    // Duyệt qua các đòn đánh từ 0 đến n-2
    for (int i = 0; i < n - 1; i++) {
        // Tính khoảng cách giữa đòn đánh hiện tại và đòn đánh kế tiếp
        int gap = timeSeries[i + 1] - timeSeries[i];
        // Cộng vào tổng giá trị nhỏ hơn giữa duration và gap
        totalDuration += min(duration, gap);
    }
    // Đòn đánh cuối cùng luôn gây ra đủ lượng duration giây độc
    totalDuration += duration;
    return totalDuration;
    }
};