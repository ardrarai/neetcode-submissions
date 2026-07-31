class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums: return None
        freq = Counter(nums)
        common, max_count = freq.most_common(1)[0]
        if max_count > len(nums)/2:
            return common
        return None
        