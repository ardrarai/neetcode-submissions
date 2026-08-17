class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        
        k = 0 #index for unique ele

        for i in range(1,len(nums)):
            if nums[i]!=nums[k]:
                k+=1
                nums[k] = nums[i]

        return k+1
      