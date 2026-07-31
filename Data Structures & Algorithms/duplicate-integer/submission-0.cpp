class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int n = nums.size(),i,j,fix,flag = 0;
        for(i=0;i<n;i++){
            fix=nums[i];
            for(j=i+1;j<n;j++){
                if(fix==nums[j]){
                    flag=1;
                    break;
                }
            }
            if(flag == 1) break;
        }
        if(flag==1)
            return 1;
        else
            return 0;
    }
};