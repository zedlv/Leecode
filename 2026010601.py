#【热题100】05-最长回文串
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = Counter(s)
        s_s = True
        i = 0
        for count in char_count.values:
            if count % 2 != 0:
                i+=1
                s_s = False
        if s_s:
            return len(s)
        else:
          return  len(s)-i+1 if i>1 else len(s)

        