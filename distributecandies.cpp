class Solution {
public:
    int distributeCandies(vector<int>& candyType) {
    unordered_set<int> uniqueCandies(candyType.begin(), candyType.end());
    
    int n = candyType.size();
    int doctorLimit = n / 2;
    int uniqueCount = uniqueCandies.size();
    return min(uniqueCount, doctorLimit);
    }
};