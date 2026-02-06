class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
        int n = arr.size();
        int zeros = 0;
        int left = 0;
        while (left <= n - 1 - zeros) {
            if (arr[left] == 0) {
                if (left == n - 1 - zeros) {
                    arr[n - 1] = 0;
                    n--;
                    break;
                }
                zeros++;
            }
            left++;
        }
        int j = n - 1 - zeros;
        for (int k = n - 1; j >= 0; j--) {
            if (arr[j] == 0) {
                arr[k--] = 0;
                arr[k--] = 0;
            } else {
                arr[k--] = arr[j];
            }
        }
    }
};