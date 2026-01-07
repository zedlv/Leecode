# 赎金信·判断是否可以由杂志中的字符构成
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_dict = {}
        magazine_dict = {}
        for i in ransomNote:
            if i in ransomNote_dict:
                ransomNote_dict[i] += 1
            else:
                ransomNote_dict[i] = 1
        for i in magazine:
            if i in magazine_dict:
                magazine_dict[i] += 1
            else:
                magazine_dict[i] = 1
        for i in ransomNote_dict:
            if i not in magazine_dict or ransomNote_dict[i] > magazine_dict[i]:
                return False
        return True