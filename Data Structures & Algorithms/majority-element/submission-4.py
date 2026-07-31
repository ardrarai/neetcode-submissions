class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #if not nums: return None
        #freq = Counter(nums)
        #common, max_count = freq.most_common(1)[0]
        #if max_count > len(nums)/2:
        #    return common
        #return None
        

        #Boyer-Moore Algorithm
        res,count=0,0
        for n in nums:
            if count==0:
                res=n
            count += (1 if n==res else -1)
        return res