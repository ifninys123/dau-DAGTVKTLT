class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
    int n = nums.size();
    for (int i = n / 2 - 1; i >= 0; i--) {
        int parent = i;
        while (parent * 2 + 1 < n) {
            int child = parent * 2 + 1; 
            if (child + 1 < n && nums[child] < nums[child + 1]) {
                child++;
            }
            if (nums[parent] >= nums[child]) break;
            
            swap(nums[parent], nums[child]);
            parent = child;
        }
    }
    for (int i = n - 1; i > 0; i--) {
        swap(nums[0], nums[i]);
        int parent = 0;
        while (parent * 2 + 1 < i) {
            int child = parent * 2 + 1;
            if (child + 1 < i && nums[child] < nums[child + 1]) {
                child++;
            }
            if (nums[parent] >= nums[child]) break;

            swap(nums[parent], nums[child]);
            parent = child;
        }
    }
    return nums;
    }
};