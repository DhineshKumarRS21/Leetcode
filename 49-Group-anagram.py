class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for word in strs:
            key=''.join(sorted(word))
            if key not in d:
                d[key]=[]
            d[key].append(word)
        return list(d.values())


# Other solution
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            groups[tuple(count)].append(word)
        return list(groups.values())
