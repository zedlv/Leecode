class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 【1、定义需要维护的变量】
        result = 0
        # 【2、定义窗口的首尾端 (start, end)，然后滑动窗口】
        left = 0
        # 同时又涉及去重，因此需要一个哈希表
        hash = set()
        #  窗口的右端位置从 0 开始，可以一直移动到尾部
        for right in range(len(s)):
            # 【3、更新需要维护的变量, 有的变量需要一个 if 语句来维护 (比如最大最小⻓度)】
            # # 【4、如果题目的窗口⻓度可变: 这个时候一般涉及到窗口是否合法的问题】
            # #  如果当前窗口不合法时, 用一个 while 去不断移动窗口左指针, 从而剔除非法元素直到窗口再次合法
            while s[right] in hash:
                hash.remove(s[left])
                left+=1
            hash.add(s[right])
            result = max(result, right-left+1)
        # 【5、返回所需要的答案】
        return result