class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n=len(strs)
        res=defaultdict(list)
        for i in range(n):
            sort="".join(sorted(strs[i]))
            res[sort].append(strs[i])
        return list(res.values())