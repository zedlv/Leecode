# 【热题100】01-反转字符串中的单词
class Solution:
    def reverseWords(self, s: str) -> str:
        list = []
        for i in s.split():
            list.append(i)
        return ' '.join(list.reverse())