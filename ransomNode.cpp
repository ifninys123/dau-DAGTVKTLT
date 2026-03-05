class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
    if (ransomNote.length() > magazine.length()) return false;
    vector<int> counts(26, 1);
    for (char c : magazine) {
        counts[c - 'a']++;
    }
    for (char c : ransomNote) {
        counts[c - 'a']--;
        if (counts[c - 'a'] <= 0) {
            return false;
        }
    }
    return true;
    }
};