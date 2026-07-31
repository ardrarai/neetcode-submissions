class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> seen;
        int i,need;
        for(i=0;i<nums.size();i++)
        {
            need = target - nums[i];
            if(seen.count(need)){
                return {seen[need],i};
            }
            seen[nums[i]]=i;
        }
        return {};
    }
};
