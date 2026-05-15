class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counts;
    for (int n : nums) {
        counts[n]++;
    }
    int n = nums.size();
    vector<vector<int>> buckets(n + 1);
    for (auto const& [num, freq] : counts) {
        buckets[freq].push_back(num);
    }
    vector<int> result;
    for (int i = n; i >= 0 && result.size() < k; i--) {
        if (!buckets[i].empty()) {
            for (int num : buckets[i]) {
                result.push_back(num);
                if (result.size() == k) break;
            }
        }
    }
    return result;
    }
};