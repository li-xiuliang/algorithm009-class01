class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        count = collections.defaultdict(list)
        [count[tuple(sorted(strs[i]))].append(strs[i]) for i in range(len(strs))]
        return list(count.values())