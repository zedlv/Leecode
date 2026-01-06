#【热题100】04-字母异位词分组
import collections
import typing
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res =  defaultdict(list)
        for s in strs:
            res(tuple(sorted(s))).append(s)
        return res.values()
