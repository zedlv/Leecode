# 【热题100】04-最小覆盖子串
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countS = Counter(s)
        need = leng(countS)
        have = 0
        left=-1
        win_dict = {}
        leng = float('inf')
        i = 0
        for j in range(len(s)):
            chr = s[j]
            if chr in countS:
                win_dict[chr] = win_dict.get(chr,0) + 1
                if win_dict[chr] == countS[chr]:
                    have += 1
            while have  == need:
                if j-i+1 < leng:
                    left = i
                    leng = j-i+1
                if s[i] in win_dict:
                    win_dict[s[i]] -= 1
                    if win_dict[s[i]] < countS[s[i]]:
                        have -= 1
                i += 1
        return s[left:left+leng] if leng != float('inf') else ""
