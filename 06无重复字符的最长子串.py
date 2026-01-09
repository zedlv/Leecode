#【热题100】06-无重复字符的最长子串
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        hash_set = set()
        result = 0
        for right in range(len(s)):
            while s[right] in hash_set:
                hash_set.remove(s[left])
                left +=1
            hash_set.add(s[right])
            result = max(result,right-left+1)
        return result