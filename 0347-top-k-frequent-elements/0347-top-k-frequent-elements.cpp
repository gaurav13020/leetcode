class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        vector<vector<int>> freq(nums.size() + 1);
        vector<int> res;

        for (int n : nums) {
            count[n]++;
        }

        for (const auto& entry : count) {
            freq[entry.second].push_back(entry.first);
        }

        for (int i = freq.size() - 1; i > 0; --i) {
            for (int n : freq[i]) {
                res.push_back(n);
                if (res.size() == k) {
                    return res;
                }
            }
        }
        return res;
            
    }
};