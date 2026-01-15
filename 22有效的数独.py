from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 检查每一行
        for i in range(9):
            row = board[i]
            if not self.isValid(row):
                return False
        
        # 检查每一列
        for j in range(9):
            col = [board[i][j] for i in range(9)]  # 提取第j列的所有元素
            if not self.isValid(col):
                return False
        
        # 检查每个3x3子数独
        for i in range(0, 9, 3):  # 子数独左上角的行坐标：0,3,6
            for j in range(0, 9, 3):  # 子数独左上角的列坐标：0,3,6
                # 提取3x3子数独的所有元素
                subgrid = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not self.isValid(subgrid):
                    return False
        
        return True
    
    # 辅助函数：检查一个列表（行/列/子数独）是否符合数独规则
    def isValid(self, elements: List[str]) -> bool:
        seen = set()  # 用集合记录已出现的数字，快速判断重复
        for elem in elements:
            if elem == '.':  # 空位置跳过，不影响有效性
                continue
            # 规则1：非空元素必须是1-9（题目输入保证时可省略，但加上更健壮）
            if not elem.isdigit() or int(elem) < 1 or int(elem) > 9:
                return False
            # 规则2：非空元素不能重复出现
            if elem in seen:
                return False
            seen.add(elem)
        return True