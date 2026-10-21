from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for s in strs:
            # Sort the string to create a canonical key
            canonical_key = "".join(sorted(s))
            anagram_map[canonical_key].append(s)
        return list(anagram_map.values())
