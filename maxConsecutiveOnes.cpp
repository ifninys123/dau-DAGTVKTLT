class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int maxCount = 0;     // Lưu số lượng 1 liên tiếp lớn nhất
    int currentCount = 0; // Đếm số lượng 1 trong chuỗi hiện tại

    for (int num : nums) {
        if (num == 1) {
            currentCount++;
            // Luôn cập nhật maxCount mỗi khi currentCount tăng
            maxCount = max(maxCount, currentCount);
        } else {
            // Gặp số 0, reset biến đếm hiện tại
            currentCount = 0;
        }
    }

    return maxCount;
    }
};