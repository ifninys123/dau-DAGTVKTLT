class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        // 1. Lưu các loại đá quý vào một tập hợp để tìm kiếm nhanh
    unordered_set<char> jewelSet(jewels.begin(), jewels.end());
    
    int count = 0;
    
    // 2. Duyệt qua từng viên đá bạn đang có
    for (char s : stones) {
        // Nếu viên đá này có trong tập hợp đá quý
        if (jewelSet.count(s)) {
            count++;
        }
    }
    
    return count;
    }
};