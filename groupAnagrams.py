class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in range(len(strs)):
            sortedString = tuple(sorted(strs[i]))
            if sortedString not in hashmap:
                hashmap[sortedString] = []
            hashmap[sortedString].append(strs[i])
        return list(hashmap.values())