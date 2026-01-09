# 最长公共前缀
# https://leetcode.cn/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        pre = strs[0]
        for i in strs[1:]:
            while not i.startswith(pre[:len(pre)]):
                pre = pre[:-1]
                if pre == "":
                    return ""
        return pre
