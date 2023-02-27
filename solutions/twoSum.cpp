class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::map<int,int> numap;
        std::vector<int> soln;
        for (int i = 0; i < nums.size(); i++){
            int diff = target - nums[i];
            if (numap.contains(diff)){
                soln.insert(numap.find(i));
                soln.insert(numap.find(diff));
            }
            numap.insert({nums[i], i});
        }
    return soln;
    }
};