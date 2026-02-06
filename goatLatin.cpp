class Solution {
public:
    string toGoatLatin(string sentence) {
        unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        stringstream ss(sentence);
        string word;
        string result = "";
        string suffixA = "a";
        while (ss >> word) {
            char firstChar = word[0];
            if (vowels.count(firstChar)) {
                word += "ma";
            } else {
                word = word.substr(1) + firstChar + "ma";
            }
            word += suffixA;
            suffixA += "a";
            if (result != "") result += " ";
            result += word;
        }
        return result;
    }
};