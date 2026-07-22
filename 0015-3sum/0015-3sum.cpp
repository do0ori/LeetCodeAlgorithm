class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        vector<vector<int>> result;

        for (int i = 0; i < n - 2; i++) {
            // prune
            if (nums[i] > 0) break;

            // skip duplicated number
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            // 2Sum
            int j = i + 1, k = n - 1;
            while (j < k) {
                int s = nums[i] + nums[j] + nums[k];

                if (s == 0) {
                    result.push_back({nums[i], nums[j], nums[k]});
                    j++; k--;
                    while (j < k && nums[j] == nums[j - 1]) j++;
                    while (j < k && nums[k] == nums[k + 1]) k--;
                } else if (s < 0) {
                    j++;
                } else {
                    k--;
                }
            }
        }

        return result;
    }
};