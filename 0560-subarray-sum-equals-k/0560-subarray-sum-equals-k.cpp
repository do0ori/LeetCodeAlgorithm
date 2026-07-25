class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        map<int, int> sum_count;
        sum_count[0] = 1;
        int answer = 0, sum = 0;
        for (const int& num : nums) {
            sum += num;
            answer += sum_count[sum - k];
            sum_count[sum] += 1;
        }
        return answer;
    }
};